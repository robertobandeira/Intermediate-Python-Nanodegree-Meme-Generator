"""Module that handles image manipulation and quote to image."""
from PIL import Image, ImageDraw, ImageFont
import random


class MemeEngine():
    """Class that encamsulates body, quote and image as meme."""

    def __init__(self, tmp_path):
        """Instantiate by setting a path for the temp images."""
        self.tmp_path = tmp_path

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Handle image manipulation and add quote to image."""
        if width > 500:
            width = 500

        with Image.open(img_path) as im:
            ratio = width/float(im.size[0])
            height = int(ratio*float(im.size[1]))
            im_resized = im.resize((width, height), Image.NEAREST)
        # print(text)
        # font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
        draw = ImageDraw.Draw(im_resized)
        random_x = random.randint(10, width - len(text))
        random_y = random.randint(30, height - 30)
        draw.text((random_x, random_y), f'{text} - {author}', fill='white')

        temp_file = f'{self.tmp_path}/{random.randint(0,1000000)}.jpeg'
        im_resized.save(temp_file, "JPEG")
        return temp_file
