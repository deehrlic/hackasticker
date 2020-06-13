from PIL import Image, ImageDraw, ImageFont
import random
import os

def makeImage(name, image):
    rand = random.randint(1,6)
    fname = "static/mlh_SAMPLE" + str(rand) + ".png"

    template = Image.open(fname)
    safe = template.copy()

    dum = Image.open("static/big_samples/"+image)

    dum = dum.resize((150,150),Image.ANTIALIAS)

    safe.paste(dum, (175,300))

    safe.save('static/rendered_stickers/'+name+'.png')



for filename in os.listdir('static/big_samples'):
    makeImage(filename[:-4],filename)
