import re
import os

def texts():
    mass = []
    start_path = "./news/"
    for root, dirs, files in os.walk(start_path):
        for file in files:
            path = start_path + file
            with open(path, encoding='utf-8') as f:
##                text = re.search('<body>(.+)</body>', f.read(), flags=re.DOTALL)
                text = re.sub(' \n', '\n', f.read())
                text = re.sub('`', '' ,text)
                bigr = re.findall('<ana lex="[а-яА-Я0-9]+" gr="NUM.+"></ana>([а-яА-Я0-9]+</w>\n<w><ana lex=".+" gr="S,.+,gen"></ana>\w+)</w>', text)
                doc = re.search('content="(.+)" name="docid"></', text)
                topic = re.search('content="(.+)" name="topic"', text)
                for s in bigr:
                    bi = re.search('([а-яА-Я0-9]+)</w>\n<w><ana lex=".+" gr="S,.+,gen"></ana>(\w+)', s)
                    with open('table.csv', 'w', encoding='cp1251') as f:
                        f.write(str(doc.groups(0))+';'+str(bi.groups(0))+';'+str(topic.groups(0))+'\n')
    return f
        

                

##def create(mass):
##    with open('table.csv', 'w', encoding='utf-8') as f:
##        for bi in mass:
##            f.write(
##                        
##
##                        
####                        with open ('new000.txt', 'a', encoding = 'utf-8') as f:
####                            	f.write(str(s.group(1))+' '+str(s.group(2))+'\t'+str(sent)+'\n')
##    return f


f = texts()


print('ok')

