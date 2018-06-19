import re
import os

def texts():
    mass = []
    start_path = "./news/"
    for root, dirs, files in os.walk(start_path):
        for file in files:
            path = start_path + file
            with open(path) as f:
                text = re.search('<body>(.+)</body>', f.read(), flags=re.DOTALL)
                bigr = re.findall('<se>.*<w><ana .+ gr="S.+"></ana>.+</w>\n<w><ana .+ gr="S,.+,gen"></ana>.+</w>.*</se>', str(text[0]), flags= re.DOTALL)
                for sentence in bigr:
                    sentence = re.sub('`', '', sentence)
                    sent = re.findall('<ana .+ gr="S.+"></ana>(\w+</w>\n<w><ana .+ gr="S,.+,gen"></ana>\w+)</w>', sentence)
                    for s in sent:
                        whole=re.sub('</?\w+[><]*(?:ana lex=".+" gr=".+")*>', '', sentence)
                        wh = re.sub('\n', ' ', whole)
                        print(wh)
                        s = re.search('(\w+)</w>\n<w><ana .+ gr="S,.+,gen"></ana>(\w+)', s)
##                        with open ('new000.txt', 'a', encoding = 'utf-8') as f:
##                            	f.write(str(s.group(1))+' '+str(s.group(2))+'\t'+str(sent)+'\n')
    return f


f = texts()


print('ok')



