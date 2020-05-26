from dcm2jpg import convert, extract

image = "./data/bmode.dcm"
newImage = "ttfm.jpg"
message = "message.txt"

convert(image, newImage)
extract(image, message)
