ipm0 = 0
with open('freq.txt', encoding = 'utf - 8') as f:
    for line in f:
        splitted_line = line.split(' | ')
        morf = splitted_line[1]
        gen = morf.split()

        if len(gen)>=4 and gen[3] == 'жен':
            print(splitted_line[0])
            ipm = list(splitted_line[2].strip())
            ipm = float(ipm[0])
            ipm0 += ipm
    print(ipm0)
           
