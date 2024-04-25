import cv2
import numpy as np


# Constants
CHAR_HEIGHT = 16
CHAR_WIDTH = 6
ASCII_BY_BRIGHTNESS = r'$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`''....        '
NUMBER_OF_ASCII = len(ASCII_BY_BRIGHTNESS)


def resize_img(img):
    img_height, img_width = img.shape[0], img.shape[1]
    chars_y = img_height // CHAR_HEIGHT
    chars_x = img_width // CHAR_WIDTH
    img_resized_height = chars_y * CHAR_HEIGHT
    img_resized_width = chars_x * CHAR_WIDTH
    return img[0:img_resized_height, 0:img_resized_width], chars_x, chars_y


# Load an image
image = cv2.imread('test1.jpg')

resized_image, num_of_chars_x, num_of_chars_y = resize_img(image)

gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

new_img = np.zeros((num_of_chars_y, num_of_chars_x))

for x in range(0, gray_image.shape[1], CHAR_WIDTH):
    for y in range(0, gray_image.shape[0], CHAR_HEIGHT):
        img_part = gray_image[y:y + CHAR_HEIGHT, x:x + CHAR_WIDTH]
        part_avg = np.average(img_part)
        new_img[y // CHAR_HEIGHT, x // CHAR_WIDTH] = part_avg

for y in range(0, num_of_chars_y):
    for x in range(0, num_of_chars_x):
        ASCII_brightness = (new_img[y, x] * NUMBER_OF_ASCII // 255).astype(int)
        print(ASCII_BY_BRIGHTNESS[min(ASCII_brightness, NUMBER_OF_ASCII - 1)], end='')
    print()

cv2.imshow('Original', resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
