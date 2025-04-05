from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Protocol.KDF import PBKDF2
import os

# Derive key from password
def get_key_from_password(password, salt=None):
    if salt is None:
        salt = get_random_bytes(16)
    key = PBKDF2(password, salt, dkLen=32)  # 256-bit key
    return key, salt

# Function to encrypt a file
def encrypt_file(file_path, password):
    key, salt = get_key_from_password(password)
    cipher = AES.new(key, AES.MODE_EAX)
    with open(file_path, 'rb') as f:
        data = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(data)
    
    with open(file_path + ".enc", 'wb') as f:
        f.write(salt)  # Write salt first
        f.write(cipher.nonce)
        f.write(tag)
        f.write(ciphertext)
    
    print(f"File {file_path} encrypted successfully.")

# Function to decrypt a file
def decrypt_file(file_path, password):
    with open(file_path, 'rb') as f:
        salt = f.read(16)
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()
    
    key, _ = get_key_from_password(password, salt)
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    
    try:
        data = cipher.decrypt_and_verify(ciphertext, tag)
        original_file = file_path.replace(".enc", "")
        with open(original_file, 'wb') as f:
            f.write(data)
        print(f"File {file_path} decrypted successfully.")
    except ValueError:
        print("Decryption failed! The password may be incorrect or the file may be corrupted.")

# Example usage
def main():
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == '1':
            file_name = input("Enter the file name to encrypt: ").strip()
            if not os.path.isfile(file_name):
                print("Error: File does not exist. Please try again.")
                continue
            password = input("Enter a password for encryption: ")
            encrypt_file(file_name, password)
        elif choice == '2':
            file_name_enc = input("Enter the file name to decrypt: ").strip()
            if not os.path.isfile(file_name_enc):
                print("Error: File does not exist. Please try again.")
                continue
            if not file_name_enc.endswith('.enc'):
                print("Error: File is not encrypted. Please provide a valid '.enc' file.")
                continue
            password = input("Enter the password for decryption: ")
            decrypt_file(file_name_enc, password)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
