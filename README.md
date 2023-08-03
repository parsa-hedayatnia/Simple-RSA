# Simple-RSA
This is a simple RSA cryptography.
Import necessary modules:

RSA from Crypto.PublicKey: Used to generate an RSA key pair.
PKCS1_OAEP from Crypto.Cipher: Used for encryption and decryption using the RSA key pair with the OAEP padding scheme.
Generate an RSA key pair with a key length of 1024 bits:

RSA.generate(1024) creates an RSA key pair with a modulus size of 1024 bits.
The key pair consists of a public key and a private key.
Get the public and private keys:

key_pair.publickey() returns the public key.
key_pair.export_key() returns the private key in PEM format.
Create a cipher object using the public key:

PKCS1_OAEP.new(public_key) creates an RSA cipher object with the public key using the OAEP padding scheme.
Prepare the plain text to be encrypted:

The variable plain_text contains the text to be encrypted.
Encrypt the plain text using the public key:

cipher.encrypt(plain_text) encrypts the plain text using the RSA cipher object and returns the encrypted data.
Decrypt the cipher text using the private key:

PKCS1_OAEP.new(key_pair) creates an RSA cipher object with the private key using the OAEP padding scheme.
private_cipher.decrypt(cipher_text) decrypts the cipher text using the RSA cipher object with the private key and returns the original plain text.
Print the results:

The original plain text, the encrypted cipher text, and the decrypted text are printed to the console.
Please note that RSA encryption is a public-key encryption algorithm, where the public key is used for encryption, and the private key is used for decryption. The OAEP (Optimal Asymmetric Encryption Padding) scheme is used for secure encryption. It's essential to keep the private key safe and not share it with anyone, as it is used for sensitive operations like decryption.
