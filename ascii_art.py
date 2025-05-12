import os
from PIL import Image

IMAGE_DIR = './images'
black_box = chr(9608)
ASCII_CHARS = '   . ,. .:- _.\'` - ::;;=^~!><-=-=*ucoie}{T][C)(|ZX"VRFWNMH%##@@'


def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.5)
    return image.resize((new_width, new_height))


def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ''
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel % len(ASCII_CHARS)]
    return ascii_str


def main():
    # handle prompt
    filenames = [f for f in os.listdir(
        IMAGE_DIR) if os.path.isfile(os.path.join(IMAGE_DIR, f))]
    message = ''
    for idx, name in enumerate(filenames):
        message += f"\n[{idx}] {name}"
    filename = input(f'Choose an image file: {message}\n')
    path = f'./images/{filenames[int(filename)]}'

    # open image
    try:
        image = Image.open(path)
    except Exception as e:
        print(f"Unable to open image: {e}")
        return

    # process image
    image = resize_image(image)
    image = image.convert('L')  # grayscale

    # convert to ASCII
    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    ascii_img = '\n'
    for i in range(0, len(ascii_str), img_width):
        ascii_img += ascii_str[i:i+img_width] + '\n'
    print(ascii_img)


if __name__ == '__main__':
    main()
