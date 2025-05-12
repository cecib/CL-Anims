import colorsys
import os
import sys
import time
import pdb

os.system('cls' if os.name == 'nt' else 'clear')

# using 256-Color mode
block_begin = "\033[48;5;"
block_end = "m\033[97m  \033[0m"

start = time.time()

# parameters
width = 25
height = 25
frame_num = 60000
frame_hold = 0.1
speed = 0.12


def rgb_to_ansi256(rgb):
    """Convert rgb (0–255) to 256-color code"""
    r, g, b = [int(round(x / 255 * 5)) for x in rgb]
    return 16 + 36 * r + 6 * g + b


def animate(rows):
    """Print rows of rainbow colors using ANSI"""
    for row in range(rows):
        # TODO fix hue jump
        depth = row/rows + ((time.time()-start)*speed % height)
        rgb = colorsys.hsv_to_rgb(depth % 1, 0.9, 0.9)
        color_code = int(rgb_to_ansi256([x*255 for x in rgb]))
        print("".join([block_begin, str(color_code), block_end]) * width)

    if frame_hold:
        time.sleep(frame_hold)


for frame in range(0, frame_num):
    # move topleft and hide cursor
    sys.stdout.write("\033[H\033[?25l")
    sys.stdout.flush()
    animate(height)

