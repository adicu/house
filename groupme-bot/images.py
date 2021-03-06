import os
import signal
import time
import subprocess
from random import randint
from PIL import Image, ImageFont, ImageDraw

TMP = "/tmp/"
OFFSET = -2  # vertically centers the text on the display
font = ImageFont.truetype("fonts/FreeSans.ttf", 16)


def display_text(text):
    """Display the given text on the scren with the colors desired.

    :param text: A list of tuples of (str, (int, int, int)).  Each tuple is a
    pair of a string of text to display, and and (R, G, B) tuple.

    Example:
        display_text([("ADI ", (255, 0, 0)), ("House", (0, 0, 255))])

    """
    filename = TMP + "tmp%s.ppm" % randint(10000, 99999)
    create_image_from_text(filename, text)
    display_image(filename)  # synchronous
    os.remove(filename)


def display_image(fn):
    """Display the PPM file with filename `fn` to the screen."""
    if 'ppm' in fn:
        subprocess.call(['led-matrix', '-t', '10', '-D', '1', '-r', '16', fn])
    else:
        p = subprocess.Popen(['led-image-viewer', '-r', '16', fn])
	time.sleep(10)
	p.kill()

def create_image_from_text(filename, text):
    """Create an image with the passed text.

    :param filename: the filename of the image to create.
    :param text: A list of tuples of (str, (int, int, int)).  Each tuple is a
    pair of a string of text to display, and and (R, G, B) tuple.

    Example:
        create_image_from_text("/tmp/tmpfile.ppm",
                               [("ADI ", (255, 0, 0)), ("House", (0, 0, 255))])

    """
    all_text = "".join(pair[0] for pair in text)
    width, _ = font.getsize(all_text)

    im = Image.new("RGB", (width + 30, 16), "black")
    draw = ImageDraw.Draw(im)

    x = 0
    for string, color in text:
        draw.text((x, OFFSET), string, color, font=font)
        x = x + font.getsize(string)[0]

    im.save(filename)
