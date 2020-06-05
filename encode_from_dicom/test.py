import LsbFileSteg
import dcm2jpg
from Crypto.Random import get_random_bytes
# key must be 16/24/32 bytes long
key = get_random_bytes(16)

filename = "./data/test.txt"

imageName = "data/ttfm.dcm"
newFilename = "ttfm.png"
decodedFilename = "decodedFile.txt"
decryptedFilename = "decryptedFile.txt"

#temporary image that dicom is converted to
imageTemp = "temp.jpg"
message = "message.txt"
cipher_text = "encryptedMessage.txt"
dcm2jpg.dcm2jpg(imageName, imageTemp, message)

print("Encrypting...")
iv = LsbFileSteg.encryptFile(message, cipher_text, key)
print("Encrypting finished")

print("Encoding message")
newImg = LsbFileSteg.encodeLSB(cipher_text, imageTemp, newFilename)
if not newImg is None:
        print("Stego image created.")

print("Decoding...")
LsbFileSteg.decodeLSB(newFilename, decodedFilename)
print("Decoding finished")

print("Decrypting...")
LsbFileSteg.decryptFile(decodedFilename, decryptedFilename, key, iv)
print("Decrypting finished")



