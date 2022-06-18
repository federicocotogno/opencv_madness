import cv2 as cv
from assets import assets
import sys


def annotate_line():
    file = assets.cat_image
    image = cv.imread(file)

    image_copy = image.copy()
    A, B = (200, 80), (450, 80)  # From: (X, Y) To: (X, Y)
    cv.line(image_copy, A, B, (0, 255, 255), thickness=3)

    cv.imshow('Line', image_copy)

    cv.waitKey()
    cv.destroyAllWindows()
    sys.exit("Finished!")


def annotate_circle():
    file = assets.cat_image
    image = cv.imread(file)

    image_copy = image.copy()
    circle_center = (300, 300)  # From: (X, Y) To: (X, Y)
    cv.circle(image_copy, circle_center, radius=200, color=(0, 255, 255), thickness=6)
    # -1 thickness fills the circle

    cv.imshow('Circle', image_copy)

    cv.waitKey()
    cv.destroyAllWindows()
    sys.exit("Finished!")


def annotate_square():
    file = assets.cat_image
    image = cv.imread(file)

    image_copy = image.copy()
    A, B = (200, 200), (450, 450)

    cv.rectangle(image_copy, A, B, (0, 255, 0), thickness=6, lineType=cv.LINE_8)

    cv.imshow('Square', image_copy)

    cv.waitKey()
    cv.destroyAllWindows()
    sys.exit("Finished!")


def annotate_text():
    file = assets.cat_image
    image = cv.imread(file)

    image_copy = image.copy()
    text = 'This is cat'
    position = (450, 300)  # X, Y starts at bottom left
    cv.putText(image_copy, text, position, fontFace=cv.FONT_HERSHEY_COMPLEX,
               fontScale=1.7, color=(0, 255, 0), thickness=2)

    cv.imshow('Text Image', image_copy)

    cv.waitKey()
    cv.destroyAllWindows()
    sys.exit("Finished!")


# T
def annotate_text_square():
    file = assets.cat_image
    image = cv.imread(file)

    image_copy = image.copy()

    # Square
    A, B = (200, 200), (450, 450)
    cv.rectangle(image_copy, A, B, (0, 255, 0), thickness=6, lineType=cv.LINE_8)

    # Text
    text = 'This is cat'
    position = (A[0], B[1] + 50)  # X, Y starts at bottom left
    cv.putText(image_copy, text, position, fontFace=cv.FONT_HERSHEY_COMPLEX,
               fontScale=1.4, color=(0, 255, 0), thickness=2)

    cv.imshow('Text Square Image', image_copy)
    cv.imwrite('output.png', image_copy)

    cv.waitKey()
    cv.destroyAllWindows()
    sys.exit("Finished!")


if __name__ == '__main__':
    annotate_text_square()
