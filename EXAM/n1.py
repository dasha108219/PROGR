print('Задание 1\n')

import re
import os

def read_f():
    start_path = "./news/"
    for root, dirs, files in os.walk(start_path):
        for f in files:
            path = start_path + f
            with open(path, 'r') as file:
                file = f.strip('.html')
                file = file +'.txt'
                with open(file, encoding = 'utf-8') as file:
                    file = file.read()
                    print(file)
                title = re.search('<title>.*</title>', file, flags = re.DOTALL)
                print(title)

                for line in file:
                    ac = re.sub('`', '', line)
                    w_tags = re.sub('</?\w+[><]*(?:ana lex=".+" gr=".+")*>', '', ac)
                    with open(file, 'w', encoding = 'cp1251') as new_doc:
                        new_doc.write(str(title)+'\n'+str(w_tags))
    return new_doc

new_doc = read_f()
    
                    
    
