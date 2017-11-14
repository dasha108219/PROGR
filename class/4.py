with open("new.txt", encoding = "utf-8") as f:
    title = f.readline().strip()
    print(title) #цикл продолжает считывать со второй строки
    for line in f.readlines():
        stripp = line.strip()
        print(len(stripp))
    if f.read() == "":
        print("Файл закончился")
