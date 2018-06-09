import re

def read_f():
    with open('mystem.xml', encoding = 'utf-8') as f:
        f = f.read()
    return f

def dic(f):
    diction = {}
    keys = re.findall('<w><ana lex=".+" gr="(.+)" />', f)
    for key in keys:
        a = re.findall(key, f)  
        value = len(a)
        diction1 = {key:value}
        diction.update(diction1)
    return diction

def write_f(diction):
    with open('new2','w', encoding = 'utf-8') as f:
        for key in sorted(diction, key=diction.get, reverse=True):
            f.write(key)
    return key

f = read_f()
diction = dic(f)
key = write_f(diction)
