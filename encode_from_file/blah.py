import LsbFileSteg
from dcm2jpg import dcm2jpg

filename = "./data/test.txt"
imageName = "./data/ttfm.dcm"
newFilename = "ttfm.png"
decodedFilename = "decodedFile"

imageTemp = "temp.jpg"
message = "message.txt" 

dcm2jpg(imageName, imageTemp, message)  
print("Encoding...")
img = LsbFileSteg.encodeLSB(message, imageTemp, newFilename)
print("Encoding finished.")

print("Decoding...")
LsbFileSteg.decodeLSB(newFilename, decodedFilename)
print("Decoding finished.")
