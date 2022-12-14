import sys
from PIL import Image, ImageOps
from os.path import splitext

def main():
    check_image_file()
    try:
        image = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirt = Image.open("shirt.png")
    size = shirt.size
    image_r = ImageOps.fit(image, size)
    image_r.paste(shirt, shirt)
    image_r.save(sys.argv[2])


def check_image_file():
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        if len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        file1 = splitext(sys.argv[1].lower())
        file2 = splitext(sys.argv[2].lower())
        if check_ext(file1[1]) == False:
            sys.exit("Invalid input")
        if check_ext(file2[1]) == False:
            sys.exit("Invalid input")
        if file1[1] != file2[1]:
            sys.exit("Input and output have different extensions")


def check_ext(file):
    if file in [".jpg", ".jpeg", ".png"]:
        return True
    return False


main()