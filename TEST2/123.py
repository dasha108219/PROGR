import re

def read_f():
    with open('mystem.xml', encoding = 'utf-8') as f:
        f = f.read()
    return f

def ans(f):
    count = 0
    f = re.findall('<body>(.*)</body>', f, flags = re.DOTALL)
    for line in f:
        for a in line:
            count +=1
    return count

def write_f(count):
    with open('new.txt','w', encoding = 'utf-8') as file:
        file.write(str(count))
    return file

f = read_f()
count = ans(f)
file = write_f(count)
