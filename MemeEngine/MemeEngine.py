"""Module that handles image manipulation and quote to image."""
from PIL import Image, ImageDraw, ImageFont
import random
import textwrap
from string import ascii_letters


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
        font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
        draw = ImageDraw.Draw(im_resized)

        text_size_x = sum(font.getsize(character)[0] for character in ascii_letters)
        character_size_x = text_size_x / len(ascii_letters)
        max_width = int(im_resized.size[0] / (2 * character_size_x))
        random_x = random.randint(10, width - int(max_width * character_size_x))

        text_size_y = sum(font.getsize(character)[1] for character in ascii_letters)
        character_size_y = text_size_y / len(ascii_letters)
        max_height = int(im_resized.size[1] / (2 * character_size_y))
        text_wrapped = textwrap.fill(text=text, width=max_width)
        nlines = len(text_wrapped.splitlines()) + 1
        random_y = random.randint(30, height/2 - int(max_height * nlines))

        draw.text((random_x, random_y), f'{text_wrapped}\n{author}', 
                  fill='white', font=font)

        temp_file = f'{self.tmp_path}/{random.randint(0,1000000)}.jpeg'
        im_resized.save(temp_file, "JPEG")
        return temp_file
