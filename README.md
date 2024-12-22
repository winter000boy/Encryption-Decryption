# 🔐 Python Message Encryption-Decryption System

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Cryptography](https://img.shields.io/badge/Cryptography-Security-red)
![License](https://img.shields.io/badge/License-MIT-green)

A robust and secure message encryption and decryption system built with Python. This tool provides a simple yet secure way to encrypt and decrypt messages using a password-based encryption system.

**Keywords**: encryption, decryption, cryptography, python security, message encryption, data security, cipher, cryptographic algorithms, secure messaging, password-based encryption, Fernet encryption, python cryptography, secure communication

## 🚀 Features

- Password-based encryption using Fernet (symmetric encryption)
- Simple and intuitive command-line interface
- Secure message handling
- File encryption capabilities
- Cross-platform compatibility
- Default password protection
- Error handling for invalid inputs

## 📋 Prerequisites

- Python 3.7 or higher
- cryptography library : base64

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/winter000boy/Encryption-Decryption.git
```

2. Navigate to the project directory:
```bash
cd Encryption-Decryption
```

3. Install required dependency:
```bash
pip install cryptography
```

## 💻 Usage

### Important Note
The default password for encryption/decryption is: **"doit"**

### Running the Program

1. Run the script:
```bash
python main.py
```

2. Choose your option:
   - Press 1 for Encryption
   - Press 2 for Decryption
   - Press 3 to Exit

### Encryption Process
1. Select option 1
2. Enter your message to encrypt
3. Enter the password (use "doit" as default)
4. The encrypted message will be displayed

### Decryption Process
1. Select option 2
2. Enter the encrypted message
3. Enter the password (must match the encryption password)
4. The decrypted message will be displayed

### Example Usage:

```python
# Encryption Example
Enter your choice (1/2/3): 1
Enter the message to encrypt: Hello World
Enter the password: doit
Encrypted Message: gAAAAABl....[encrypted string]....

# Decryption Example
Enter your choice (1/2/3): 2
Enter the encrypted message: gAAAAABl....[encrypted string]....
Enter the password: doit
Decrypted Message: Hello World
```

## 🔒 Security Features

- Fernet symmetric encryption (based on AES)
- Password-based key derivation
- Secure message handling
- Built-in timestamp validation
- Protection against unauthorized decryption

## ⚠️ Important Security Notes

1. Always remember your password - there's no way to recover encrypted messages without it
2. The default password "doit" should be changed for production use
3. Keep your encrypted messages secure
4. Don't share your password with unauthorized users

## 🔍 Error Handling

The system handles various errors including:
- Invalid password attempts
- Corrupted encrypted messages
- Invalid input formats
- System and encryption exceptions

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

Durgesh Sharma - [sharmajdurgesh04@gmail.com]

Project Link: [https://github.com/winter000boy/Encryption-Decryption]

## 🌟 Acknowledgments

- [Python Cryptography Library](https://cryptography.io/)
- [Fernet Specification](https://github.com/fernet/spec/)
- [Security Best Practices Guide](https://www.owasp.org/)

---
**Note**: This project is for educational purposes only. For production use, please ensure proper security auditing and testing, and change the default password.

Keywords: #Python #Encryption #Decryption #Cryptography #Security #PasswordEncryption #Fernet #SecureCommunication #DataSecurity #PythonSecurity #MessageEncryption #SymmetricEncryption 