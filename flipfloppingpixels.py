from PIL import Image

def mirror_horizontal(image):
    img = Image.open(image)
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img.save("mirroredhorizontal.png")
#mirror_horizontal("biking-hero-1.png")

def mirror_vertical(image):
    img = Image.open(image)
    img = img.transpose(Image.ROTATE_180)
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img.save("mirrorvertical.png")
#mirror_vertical("biking-hero-1.png")

def mirror_four(image):
    img = Image.open(image)
    width, height = img.size
    xcord = width // 2
    ycord = height//2
    image = img.resize([(int(.5*width)), (int(.5*height))])
    flipimage = image.transpose(Image.ROTATE_180)
    horizontalimg = image.transpose(Image.FLIP_LEFT_RIGHT)
    horizontalflip = horizontalimg.transpose(Image.ROTATE_180)
    canvas = Image.new("RGB", (width, height), "white")
    canvas.paste(image)
    canvas.paste(horizontalimg, (xcord, 0))
    canvas.paste(flipimage, (xcord, ycord))
    canvas.paste(horizontalflip, (0, ycord))
    canvas.save("mirrorfour.png")
#mirror_four("biking-hero-1.png")