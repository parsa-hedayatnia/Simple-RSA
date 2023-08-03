# This is a sample Python script.
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
# Generate 1024-bit RSA key pair
key_pair = RSA.generate(1024)

# Get public and private keys
public_key = key_pair.publickey()
private_key = key_pair.export_key()

# Create a cipher object using public key
cipher = PKCS1_OAEP.new(public_key)

# Plain text to be encrypted
plain_text = "Hello, I'm Parsa Hedayatnia.I hope this code is useful for youس!"

# Encrypt the plain text
cipher_text = cipher.encrypt(plain_text)

# Decrypt the cipher text using the private key
private_cipher = PKCS1_OAEP.new(key_pair)
decrypted_text = private_cipher.decrypt(cipher_text)

print("Plain text:", plain_text)
print("Cipher text:", cipher_text)
print("Decrypted text:", decrypted_text)
