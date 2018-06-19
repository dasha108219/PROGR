import re
import os
import csv



def read_f():
    doc_id_t = []
    start_path = "./news/"
    for root, dirs, files in os.walk(start_path):
        for file in files:
            path = start_path + file
            with open(path) as f:
                f = f.readlines()
            for line in f:
                doc_id = re.search('content="(.+)" name="docid"', line)
                if doc_id != None:
                    doc_id_t.append(doc_id[1])
                    with open('table11.csv', 'w', encoding='utf-8') as file:
                        for x in doc_id_t:
                            file.write(str(x)+',')
                        file.write('\n')
    return file

def title():
    start_path = "./news/"
    for root, dirs, files in os.walk(start_path):
        for file in files:
            path = start_path + file
            with open(path) as f:
                f = f.readlines()
                title_t = []
                for line in f:
                    title = re.search('<title>(.+)</title>',line)
                    if title != None:
                        title_t.append(title.group(1))
                        with open('table11.csv', 'a', encoding='utf-8') as fil:
                            for x in title_t:
                                x= re.sub(',',';',x)
                                fil.write(x+','  )

    return fil

def author():
    start_path = "./news/"
    for root, dirs, files in os.walk(start_path):
        for file in files:
            path = start_path + file
            with open(path) as f:
                f = f.readlines()
                author_t = []
                for line in f:
                    author = re.search('content="(.+)" name="author"',line)
                    if author != None:
                        author_t.append(author.group(1))
                        with open('table11.csv', 'a', encoding='utf-8') as f:
                            f.write('\n')
                            for x in author_t:
                                f.write(x+',')
    return f

def created():
    start_path = "./news/"
    for root, dirs, files in os.walk(start_path):
        for file in files:
            path = start_path + file
            with open(path) as f:
                f = f.readlines()
                created_t=[]
                for line in f:
                    created = re.search('content="(.+)" name="created"',line)
                    if created != None:
                        created_t.append(created.group(1))
                        with open('table11.csv', 'a', encoding='utf-8') as a:
                            a.write('\n')
                            for x in created_t:
                                a.write(x+',')
         
    return a

def topic():
    start_path = "./news/"
    for root, dirs, files in os.walk(start_path):
        for file in files:
            path = start_path + file
            with open(path) as f:
                f = f.readlines()
            topic_t=[]
            for line in f:
                topic = re.search('content="(.+)" name="topic"',line)
                if topic != None:
                    topic_t.append(topic.group(1))
                    with open('table11.csv', 'a', encoding='utf-8') as c:
                        c.write('\n')
                        for x in topic_t:
                            x= re.sub(',',';',x)
                            c.write(x+',')
                        c.write('\n')
    return c

def tagging():
    start_path = "./news/"
    for root, dirs, files in os.walk(start_path):
        for file in files:
            path = start_path + file
            with open(path) as f:
                f = f.readlines()
            tagging_t=[]
            for line in f:
                tagging = re.search('content="(.+)" name="tagging"',line)
                if tagging != None:
                    tagging_t.append(tagging.group(1))
                    with open('table11.csv', 'a', encoding='utf-8') as q:
                        q.write('\n')
                        for x in tagging_t:
                            q.write(x+',')         
    return q
 

file= read_f()
fil=title()
f=author()
a=created()
c=topic()
q=tagging()
print('айл записан')
##                      author_t, created_t, topic_t, tagging_t)

