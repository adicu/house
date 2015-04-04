import time
import RPi.GPIO as GPIO

from images import display_image, display_text

delay = 0.000001

GPIO.setmode(GPIO.BCM)
red1_pin = 17
green1_pin = 18
blue1_pin = 22
red2_pin = 23
green2_pin = 24
blue2_pin = 25
clock_pin = 3
a_pin = 7
b_pin = 8
c_pin = 9
latch_pin = 4
oe_pin = 2

GPIO.setup(red1_pin, GPIO.OUT)
GPIO.setup(green1_pin, GPIO.OUT)
GPIO.setup(blue1_pin, GPIO.OUT)
GPIO.setup(red2_pin, GPIO.OUT)
GPIO.setup(green2_pin, GPIO.OUT)
GPIO.setup(blue2_pin, GPIO.OUT)
GPIO.setup(clock_pin, GPIO.OUT)
GPIO.setup(a_pin, GPIO.OUT)
GPIO.setup(b_pin, GPIO.OUT)
GPIO.setup(c_pin, GPIO.OUT)
GPIO.setup(latch_pin, GPIO.OUT)
GPIO.setup(oe_pin, GPIO.OUT)

screen = [[0 for x in xrange(32)] for x in xrange(16)]


def clock():
    GPIO.output(clock_pin, 1)
    GPIO.output(clock_pin, 0)


def latch():
    GPIO.output(latch_pin, 1)
    GPIO.output(latch_pin, 0)


def bits_from_int(x):
    a_bit = x & 1
    b_bit = x & 2
    c_bit = x & 4
    return (a_bit, b_bit, c_bit)


def set_row(row):
    a_bit, b_bit, c_bit = bits_from_int(row)
    GPIO.output(a_pin, a_bit)
    GPIO.output(b_pin, b_bit)
    GPIO.output(c_pin, c_bit)


def set_color_top(color):
    red, green, blue = bits_from_int(color)
    GPIO.output(red1_pin, red)
    GPIO.output(green1_pin, green)
    GPIO.output(blue1_pin, blue)


def set_color_bottom(color):
    red, green, blue = bits_from_int(color)
    GPIO.output(red2_pin, red)
    GPIO.output(green2_pin, green)
    GPIO.output(blue2_pin, blue)


def refresh():
    for row in range(8):
        GPIO.output(oe_pin, 1)
        set_color_top(0)
        set_row(row)
        for col in range(32):
            set_color_top(screen[row][col])
            set_color_bottom(screen[row + 8][col])
            clock()
        latch()
        GPIO.output(oe_pin, 0)
        time.sleep(delay)


def fill_rectangle(x1, y1, x2, y2, color):
    for x in range(x1, x2):
        for y in range(y1, y2):
            screen[y][x] = color


def set_pixel(x, y, color):
    screen[y][x] = color


def jettfunc(text):
    for i in range(50):
        fill_rectangle(0, 0, 32, 16, i % 8)
        refresh()


def dan(text):
    display_text(text)


def rasmi(text):
    display_image('images/RAZZLE.ppm')

functions = {}
functions['Jett Andersen'] = jettfunc
functions['Rasmi Elasmar'] = rasmi
