with open("new.txt", "w", encoding = "utf - 8") as file:
    word = input()
    while word != "":
        file.write("\n" + word) 
        word = input()
        
with open('new.txt', encoding = 'utf - 8') as file:
    with open('freq.txt', encoding = 'utf - 8') as f:
        for line in f:
            splitted_line = line.split(' | ')
            for word in file:
                word = word.strip()





