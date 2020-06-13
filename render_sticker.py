from PIL import Image, ImageDraw, ImageFont
import random

def makeImage(image):
    rand = random.randint(1,6)
    fname = "static/mlh_SAMPLE" + str(rand) + ".png"

    template = Image.open(fname)
    safe = template.copy()

    dum = Image.open("static/dummy.png")

    dum = dum.resize((300,300),Image.ANTIALIAS)

    safe.paste(dum)

    safe.save('static/safsfa.png')

makeImage(3)
