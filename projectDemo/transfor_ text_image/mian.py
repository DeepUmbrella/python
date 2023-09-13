import cv2
import numpy as np
import os

from PIL import Image


if __name__ == '__main__':

    abs_path = os.path.dirname(__file__)
    for m in range(1, 5):
        img = Image.open(os.path.join(
            abs_path, f'image_resource/nopush_0{m}.jpg'))

        RESIZE_height = 300

        img_height, image_width = img.size

        RESIZE_width = int(image_width * RESIZE_height / img_height)

        img = img.resize((RESIZE_width, RESIZE_height))

        pixels = np.array(img.convert("L"))

        chars = 'MNHQ$OC?7>!:-;. '

        N = len(chars)

        step = 256 // N

        result = ""

        for i in range(RESIZE_height):
            for j in range(RESIZE_width):
                result += chars[pixels[i][j] // step]
            result += '\n'
        with open(os.path.join(abs_path, f'image_resource/result{m}.txt'), 'w') as f:
            f.write(result)
