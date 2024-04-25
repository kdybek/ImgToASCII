import cv2
import numpy as np

# Constants
ASCII_BY_BRIGHTNESS = r'$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`''. '
NUMBER_OF_ASCII = len(ASCII_BY_BRIGHTNESS)
RGB_MAX = 255


def resize_img(img, chunk_h, chunk_w):
    chars_y, chars_x = get_size_in_chunks(img, chunk_h, chunk_w)
    img_resized_height = chars_y * chunk_h
    img_resized_width = chars_x * chunk_w
    return img[0:img_resized_height, 0:img_resized_width]


def get_size_in_chunks(img, char_h, char_w):
    img_height, img_width = img.shape[0], img.shape[1]
    return img_height // char_h, img_width // char_w


def get_chunk_averages(img, chunk_h, chunk_w):
    chunks_y, chunks_x = get_size_in_chunks(img, chunk_h, chunk_w)
    new_img = np.zeros((chunks_y, chunks_x))

    for y in range(0, img.shape[0], chunk_h):
        for x in range(0, img.shape[1], chunk_w):
            img_part = img[y:y + chunk_h, x:x + chunk_w]
            part_avg = np.average(img_part)
            new_img[y // chunk_h, x // chunk_w] = part_avg

    return new_img


def print_as_ascii(img):
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            ascii_brightness = NUMBER_OF_ASCII - ((img[y, x] * NUMBER_OF_ASCII) // RGB_MAX) - 1
            print(ASCII_BY_BRIGHTNESS[ascii_brightness.astype(int)], end='')
        print()


def convert_img(img, chunk_h, chunk_w, equalize=False):
    resized_img = resize_img(img, chunk_h, chunk_w)
    gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

    if equalize:
        gray_img = cv2.equalizeHist(gray_img)

    chunk_averages = get_chunk_averages(gray_img, chunk_h, chunk_w)
    print_as_ascii(chunk_averages)


def show_img(img, title=None):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def load_img(path):
    return cv2.imread(path)
