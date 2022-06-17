import cv2 as cv
from assets import assets
import sys


def resize_image(percent: float):
    file = assets.cat_image

    image = cv.imread(file)

    # Get image dimensions
    image_dim = image.shape  # Returns (Height, Width, NO of Channels (ex: 4 = Alpha, Red, Green, Blue))
    print('Dimensions:', image_dim)
    height, width = image_dim[0], image_dim[1]

    # Process them for resizing
    # These can also be constants (ex: 300, 200)
    new_height = int(height * percent)
    new_width = int(width * percent)
    new_dim = (new_width, new_height)

    # https://theailearner.com/2018/11/15/image-interpolation-using-opencv-python/
    # for a quick guide to image interpolation
    resized = cv.resize(image, new_dim, interpolation=cv.INTER_LINEAR)
    # Another way to scale:
    # resized = cv.resize(image, None, fx=3, fy=3, interpolation=cv.INTER_CUBIC)

    print('New dimensions:', resized.shape)
    cv.imshow('Resized Image ', resized)
    cv.waitKey(3000)

    cv.imwrite(f'resized-output.png', resized)

    cv.destroyAllWindows()
    sys.exit("Finished!")


if __name__ == '__main__':
    resize_image(percent=0.2)
