from flask import Flask, request, render_template, send_file
from sbox_core import generate_sbox
from crypto_tests import *
from encryption import *
from export import export_to_excel
import os

app = Flask(__name__)

EXPORT_FILE = "aes_export.xlsx"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    sbox_table = None
    enc_trace = None
    dec_trace = None

    if request.method == "POST":
        matrix = request.form["matrix"]
        plaintext = request.form["plaintext"]

        # Generate S-box & AES key
        sbox = generate_sbox(matrix)
        key = generate_key()

        # Prepare plaintext (1 AES block)
        pt = plaintext.encode().ljust(16, b'\x00')

        # Encrypt & decrypt with trace
        ciphertext, enc_trace = aes_encrypt_trace(pt, key, sbox)
        decrypted, dec_trace = aes_decrypt_trace(ciphertext, key, sbox)

        # Build S-box table
        sbox_table = [
            [f"{sbox[r*16 + c]:02X}" for c in range(16)]
            for r in range(16)
        ]

        # Cryptographic tests
        crypto_result = {
            "NL": nonlinearity(sbox),
            "SAC": sac(sbox),
            "BIC_NL": bic_nl(sbox),
            "BIC_SAC": bic_sac(sbox),
            "LAP": lap(sbox),
            "DAP": dap(sbox),
            "DU": differential_uniformity(sbox),
            "AD": algebraic_degree(sbox),
            "TO": transparency_order(sbox),
            "CI": correlation_immunity(sbox),
        }

        result = {
            "Key": key.hex(),
            "Plaintext": plaintext,
            "Ciphertext": ciphertext.hex(),
            "Decrypted": decrypted.rstrip(b'\x00').decode(errors="ignore"),
            **crypto_result
        }

        # Export to Excel
        export_to_excel(
            filename=EXPORT_FILE,
            affine_matrix=matrix,
            key_hex=key.hex(),
            plaintext=plaintext,
            ciphertext_hex=ciphertext.hex(),
            decrypted=result["Decrypted"],
            sbox=sbox,
            enc_trace=enc_trace,
            dec_trace=dec_trace,
            crypto_result=crypto_result
        )

    return render_template(
        "index.html",
        matrices=["K4", "K44", "K81", "K111", "K128"],
        result=result,
        sbox_table=sbox_table,
        enc_trace=enc_trace,
        dec_trace=dec_trace
    )

@app.route("/download")
def download_excel():
    if os.path.exists(EXPORT_FILE):
        return send_file(
            EXPORT_FILE,
            as_attachment=True,
            download_name="AES_Affine_Sbox_Result.xlsx"
        )
    return "File not found", 404

if __name__ == "__main__":
    app.run(debug=True)
