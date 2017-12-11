with open('freq.txt', encoding = 'utf - 8') as f:
    for line in f:
        splitted_line = line.split(' | ')
        if splitted_line[1] == 'союз':
            print(splitted_line[0])
        
