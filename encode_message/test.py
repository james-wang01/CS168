import LsbSteg
from Crypto.Random import get_random_bytes
# key must be 16/24/32 bytes long
key = get_random_bytes(16)

message = "This is a hidden text in an image"

imageFilename = "stars_background.jpg"
newImageFilename = "stego_stars_background"
print("Original message: ", message)
print("Encrypting...")
cipher_text, iv = LsbSteg.encrypt(message,key)
print("Encrypted message: ", cipher_text)

print("Encoding message")
newImg = LsbSteg.encodeLSB(cipher_text, imageFilename, newImageFilename)
if not newImg is None:
        print("Stego image created.")

print("Decoding...")
cipher_text2 = LsbSteg.decodeLSB("stego_stars_background.png")
print("Decoded (but encrypted) message: ", cipher_text2)

print("Decrypting...")
plaintext = LsbSteg.decrypt(cipher_text2, key, iv)
print("Decrypted message: ", plaintext)



