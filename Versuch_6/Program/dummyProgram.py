import Image

im = Image.open("../res/FaceRecogBilder/training/1-2.png")
print im.format, im.size, im.mode
im.show()