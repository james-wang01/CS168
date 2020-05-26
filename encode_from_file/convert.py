from dcm2jpg import convert, extract

image = "./data/ttfm.dcm"
newImage = "ttfm.jpg"
message = "message.txt"

convert(image, newImage)
extract(image, message)
