def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    marks = [",", " ", ".", "/", "*", "_", "-", ";", ":"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    s = list(plate)
    while i in s and i not in numbers:
        



main()