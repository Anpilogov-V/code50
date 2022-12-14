# Among the fonts supported by FIGlet are those at figlet.org/examples.html.

# FIGlet has since been ported to Python as a module called pyfiglet.

# In a file called figlet.py, implement a program that:

#    Expects zero or two command-line arguments:
#        Zero if the user would like to output text in a random font.
#        Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
#    Prompts the user for a str of text.
#    Outputs that text in the desired font.

# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.


import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
list = figlet.getFonts()


def main(figlet, list):
    # определяем вид sys.argv и его корректность
    a = check(list)
    if a == 1:
        font = random.choice(list)
        convert(figlet, font)
    elif a == 2:
        font = sys.argv[2]
        convert(figlet, font)
    elif a == 3:
        sys.exit("Invalid usage")


def check(list):
    if len(sys.argv) == 1:
        return 1
    elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in list:
        return 2
    else:
        return 3


def convert(figlet, font):
    x = str(input("Input: "))
    figlet.setFont(font=font)
    print("Output:\n" + figlet.renderText(x))



if __name__ == "__main__":
    main(figlet, list)
