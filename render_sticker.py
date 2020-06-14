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

    safe.save('tmp.png')

def addText(name):
    fname=random.choice(os.listdir("static/rendered_stickers"))
    template = Image.open("static/rendered_stickers/"+fname)
    safe = template.copy()

    draw = ImageDraw.Draw(safe)
    fnameF=random.choice(os.listdir("fonts"))
    print(fnameF)
    if len(name)>15:
        size = 20
        if len(name)>30:
            size = 15
    else:
        size=40
    font = ImageFont.truetype("fonts/"+fnameF, size)

    draw.text((145,420),name,(0,0,0),font=font)
    safe.save('tmp.png')


#for filename in os.listdir('static/big_samples'):
#    print(filename)
#    makeImage(filename[:-4],filename)
