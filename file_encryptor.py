import base64

def encrypt_file(input_file, output_file):
    try:
        with open(input_file, "rb") as f:
            data = f.read()
        encoded_data = base64.b64encode(data)
        with open(output_file, "wb") as f:
            f.write(encoded_data)
        print(f"[+] File encrypted successfully: {output_file}")
    except FileNotFoundError:
        print("[-] Input file not found!")

def decrypt_file(input_file, output_file):
    try:
        with open(input_file, "rb") as f:
            data = f.read()
        decoded_data = base64.b64decode(data)
        with open(output_file, "wb") as f:
            f.write(decoded_data)
        print(f"[+] File decrypted successfully: {output_file}")
    except FileNotFoundError:
        print("[-] Input file not found!")
    except Exception:
        print("[-] Error: File is not properly encrypted or corrupted.")

if __name__ == "__main__":
    print("=== File Encryption Tool ===")
    print("1. Encrypt a File")
    print("2. Decrypt a File")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        inp = input("Enter input file name: ")
        out = input("Enter output encrypted file name: ")
        encrypt_file(inp, out)
    elif choice == "2":
        inp = input("Enter encrypted file name: ")
        out = input("Enter output decrypted file name: ")
        decrypt_file(inp, out)
    else:
        print("Invalid choice!")
