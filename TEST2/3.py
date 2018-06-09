import re

def read_f():
    with open('mystem.xml', encoding = 'utf-8') as f:
        f = f.read()
    return f

def count(f):
    num = re.findall('V,сов,.*ед', f)
    return num

def write_f(num):
    with open('new3.txt', 'w', encoding = 'utf-8') as file:
        file.write(str(len(num)))
    return file

f = read_f()
num = count(f)
file = write_f(num)
