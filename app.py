from flask import Flask, request, render_template
from sbox_core import generate_sbox
from crypto_tests import *
from encryption import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    sbox_table = None

    if request.method == "POST":
        matrix = request.form["matrix"]
        plaintext = request.form["plaintext"]

        # Generate S-box
        sbox = generate_sbox(matrix)

        # Key generation
        key = generate_key()

        # Encryption & decryption
        ciphertext = encrypt(plaintext, sbox, key)
        decrypted = decrypt(ciphertext, sbox, key)

        # Cryptographic test results
        result = {
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
            "Ciphertext": ciphertext.hex(),
            "Decrypted": decrypted
        }

        # Build S-box table (16x16 hex)
        sbox_table = [
            [f"{sbox[row * 16 + col]:02X}" for col in range(16)]
            for row in range(16)
        ]

    return render_template(
        "index.html",
        matrices=["K4", "K44", "K81", "K111", "K128"],
        result=result,
        sbox_table=sbox_table
    )

if __name__ == "__main__":
    app.run(debug=True)
