from flask import Flask, render_template, request
from module_1.aggregator import run_all_tests
from module_2.encrypt import encrypt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = run_all_tests()
    ciphertext = None
    plaintext = ""
    key = ""

    if request.method == "POST":
        plaintext = request.form.get("plaintext", "")
        key = request.form.get("key", "")

        if plaintext and key:
            ciphertext = encrypt(plaintext, key)

    return render_template(
        "index.html",
        results=results,
        ciphertext=ciphertext,
        plaintext=plaintext,
        key=key
    )

if __name__ == "__main__":
    app.run(debug=True)
