print('Вариант 2\n')

import os
import re

count = 0
start_path = '.'
for dirs in os.walk(start_path):
    pp = dirs[1]
    for x in pp:
        if re.search(r'[a-zA-Z]', x) == None:
            count += 1

print('Папок с кириллическим названием: ', count)
    
