with open("new.txt", encoding = "utf-8") as file:
    s = file.read()
s = s.replace(",", "").replace(".", "")
words = s.split()
print(words)
print(s.lower().count("па"))

#generation выражения
