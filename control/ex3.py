with open('text.txt', 'w', encoding = 'utf - 8') as f:
    word = input()
    while word != '':
        f.write(word)
        f.write("\n")
        word = input()
with open('freq.txt', encoding = 'utf - 8') as file:
    for line in file:
        splitted_line = line.split(' | ')
        word_dict = splitted_line[0]
        with open('text.txt',  encoding = 'utf - 8') as s:
            for word in s:
                if word.strip() == word_dict:
                    print(word, splitted_line[1], splitted_line[2])
                    
        
