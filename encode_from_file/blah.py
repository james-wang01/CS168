import LsbFileSteg

filename = "./data/test.txt"
imageName = "./data/stars_background.jpg"
newFilename = "stego_stars_background.png"
decodedFilename = "decodedFile"

print("Encoding...")
img = LsbFileSteg.encodeLSB(filename, imageName, newFilename)
print("Encoding finished.")

print("Decoding...")
LsbFileSteg.decodeLSB(newFilename, decodedFilename)
print("Decoding finished.")
