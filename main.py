import argparse
from img_processor import load_img, convert_img, show_img


def ask_yes_no_question(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in {'y', 'n', 'yes', 'n'}:
            return answer == 'y' or answer == 'yes'
        else:
            print("Please enter 'yes' or 'no'.")


def main():
    parser = argparse.ArgumentParser(description="image to ascii converter")

    parser.add_argument('path', type=str, help='Path to the image')
    parser.add_argument('chunk_h', type=int, help='Height of a chunk')
    parser.add_argument('chunk_w', type=int, help='Width of a chunk')

    args = parser.parse_args()

    equalize = ask_yes_no_question("Equalize the image before conversion?")
    show_original = ask_yes_no_question("Show original image?")

    img = load_img(args.path)
    convert_img(img, args.chunk_h, args.chunk_w, equalize)

    if show_original:
        show_img(img)


if __name__ == '__main__':
    main()
