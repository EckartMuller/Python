from rembg import remove

inputPath = "image.jpg"
outputPath = "output.png"
#rb -> read binary(Data şeklinde açar)
#wb -> write binary
with open(inputPath, "rb") as i:
    with open(outputPath,"wb") as o:
        inputFile = i.read()
        outputFile = remove(inputFile)
        o.write(outputFile)