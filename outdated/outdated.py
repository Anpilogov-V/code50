date = str(input("Date: "))
x = date[-5]
if date[-5] == "/":
    date = date.split("/")
    date[0], date[1] = float(c), float(d)
    print(f"{date[2]:2f}-{date[0]}-{date[1]}")
else:
    print("fok uuuuuuuuuuuuuuuuuuu")