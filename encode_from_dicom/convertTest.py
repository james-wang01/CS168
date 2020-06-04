from dcm2jpg import convert, extract

image = "./data/bmode.dcm"
newImage = "ttfm.jpg"
message = "message.txt"

#takes DICOM and gives the converted JPEG image
convert(image, newImage)

#extracts information from DICOM
extract(image, message)
