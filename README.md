# Endryptor

Endryptor is a simple yet powerful tool for encrypting and decrypting files using Python. This program ensures that your sensitive data remains secure by providing easy-to-use encryption and decryption functionalities.

## Features

- Encrypt files with a strong encryption algorithm
- Decrypt files to their original state
- Easy-to-use command-line interface

## Requirements

- Python 3.x
- Required Python libraries (listed in `requirements.txt`)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/rayhannm/endryptor.git
```

2. Navigate to the project directory:
```bash
cd endryptor
```
3. Run the file:
```bash
python file.py
```

## Usage

Encrypting and Decyrpting a File:

To encrypt or decrypt a file, choose option 1 or option 2. 

```bash
Choose an option:
1. Encrypt a file
2. Decrypt a file
3. Exit
Enter your choice (1/2/3):
```

Enter a password. This will be used to encrypt and decrypt the file.
```bash
Enter your choice (1/2/3): 1
Enter the file name to encrypt: test.py            
Enter your password: 
File test.py encrypted successfully.
```
Encrypted file will automatically end with `.enc`
```bash
Enter your choice (1/2/3): 2
Enter the file name to decrypt: test.py.enc
Enter your password: 
File test.py.enc decrypted successfully
```






