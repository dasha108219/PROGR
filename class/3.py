with open("new.txt", encoding = "utf-8") as f:
    lines = f.readlines()
print(lines[2].strip()) #обрезает все пробельные символы


with open("new.txt", encoding = "utf-8") as f:
    text = f.read()
lines = text.splitlines()
#lines = text.split("\n")
print(lines)


with open("new.txt", encoding = "utf-8") as f:
    lines = f.read().splitlines()
print(lines)


