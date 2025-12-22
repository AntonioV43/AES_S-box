# AES S-Box Modification

This project implements a **modified AES S-Box** using **8×8 matrix transformations**, equipped with **comprehensive cryptographic testing** to evaluate its security properties. The system provides encryption and decryption functionality, cryptographic analysis, and data export features through a web-based interface.

---

## 🔐 Features

- Modified AES S-Box generation using 8×8 matrices
- AES-based encryption and decryption
- Cryptographic evaluation, including:
  - Nonlinearity
  - Strict Avalanche Criterion (SAC)
  - Bit Independence Criterion (BIC)
  - Differential Uniformity
- Export cryptographic test results to Excel
- Web-based interface for interactive testing
- Ready for local execution and cloud deployment (Vercel)

---

## 🗂 Project Structure

```
project/
│
├── app.py # Main application entry point
├── sbox_core.py # Core S-Box generation and transformation logic
├── crypto_tests.py # Cryptographic evaluation and testing functions
├── encryption.py # Encryption and decryption implementation
├── export.py # Export test results to Excel
├── requirements.txt # Python dependencies
├── vercel.json # Vercel deployment configuration
│
├── templates/
│ └── index.html # Web interface template
│
├── static/
│ ├── style.css # Application styling
│ └── script.js # Client-side logic
│
└── README.md # Project documentation
```

---

## ⚙️ Installation

### 1. Create a Virtual Environment

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

```
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### Running the Application

```
python app.py
```

---
## 🌐 Results & Deployments

Cryptographic test results can be exported to Excel (.xlsx) format using the export feature implemented in export.py.
The generated file is created temporarily and excluded from version control.

<a href="https://aes-s-box.vercel.app" target="_blank" rel="noopener noreferrer">
Live Demo
</a>
