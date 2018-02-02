print('Вариант 2', "\n")

## сколько в тексте разных существительных
## с суффиксом -ness и какое существительное из них
## имеет максимальную частотность.

def words_with_ness(fname):
    with open('1.txt', encoding = "utf-8") as file:
        file = file.read()
    file = file.lower()
    symbols = '.,:;!?-""'''
    for s in symbols:
        file = file.replace(s, '')
    words = file.split()
    return words

def word_freq(words):
    counts = {}
    for x in words:
        if x[-4:] == 'ness':
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
    return counts

def values_pop(counts): #если нужно одно слово, то через сортировку словаря с выводом первого элемента; 
    empty = [] #массив-чтобы записывать слова с одинаковой максимальной частотностью
    maximum = max(counts.values()) 
    for key, value in counts.items():
        if value > maximum:
            maximum = value
            empty.append(key)
        elif value == maximum:
            empty.append(key)
    return empty

words = words_with_ness('1.txt')
counts = word_freq(words)
first = len(counts)
second = values_pop(counts)

print('Разных существительных с суффиксом -ness : ', first)
print('Слово/слова с максимальной частотностью: ', second)


