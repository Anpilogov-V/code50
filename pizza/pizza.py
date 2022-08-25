import tabulate
import sys
import csv

while True:
    try:
        if len(sys.argv) == 1:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1].endswith(".csv") == False:
            sys.exit("Not a Python file")
        else:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                print(tabulate(reader, headers="firstrow", tablefmt="grid"))
                break
    except FileNotFoundError:
        sys.exit("File does not exist")

