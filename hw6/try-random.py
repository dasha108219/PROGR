print('ВАРИАНТ 2')
print('Текст должен представлять собой стихотворение на русском языке из четырёх строк без рифмы, но написанное с соблюдением одной метрической схемы, кроме трёхстопного анапеста- трехстопный дактиль')
print()
import random

with open('noun_sg.txt') as file:
    file = file.read().split(' ')
    noun_sg = file
with open('noun_pl.txt') as file:
    file = file.read().split(' ')
    noun_pl = file
def noun(number):
    if number == 's':
        return random.choice(noun_sg)
    else:
        return random.choice(noun_pl)

with open('verb_ntrans_sg.txt') as file:
    file = file.read().split(' ')
    verb_ntrans_sg = file
with open('verb_trans_sg.txt') as file:
    file = file.read().split(' ')
    verb_trans_sg = file
with open('verb_ntrans_pl.txt') as file:
    file = file.read().split(' ')
    verb_ntrans_pl = file
with open('verb_trans_pl.txt') as file:
    file = file.read().split(' ')
    verb_trans_pl = file
def verb(trans, number):
    if trans == 'y':
        if number == 's':
            return random.choice(verb_trans_sg)
        else:
            return random.choice(verb_trans_pl)
    else:
        if number == 's':
            return random.choice(verb_ntrans_sg)
        else:
            return random.choice(verb_ntrans_pl)

with open('marks.txt') as file:
    file = file.read().split(' ')
    marks = file        
def punctuation():
    return random.choice(marks)

with open('addition.txt') as file:
    file = file.read().split(' ')
    addition = file
with open('adverbs.txt') as file:
    file = file.read().split(' ')
    adverbs = file    
def add(trans):
    if trans == 'y':
        return random.choice(addition)
    else:
        return random.choice(adverbs)

with open('imperative.txt') as file:
    file = file.read().split(' ')
    imperativ = file
def imperative():
    return random.choice(imperativ)


def verse1():
    return noun('s')+' '+verb('y','s')+' ' + add('y') + punctuation()
def verse2():
    return noun('p')+' '+verb('y','p')+' ' + add('y') + punctuation()
def verse3():
    return noun('s')+' '+verb('n','s')+' ' + add('n') + punctuation()
def verse4():
    return noun('p')+' '+verb('n','p')+' ' + add('n') + punctuation()
def verse5():
    return imperative()+' '+add('y')+' ' + add('n') + punctuation()

def make_verse():
    verse = random.choice([1,2,3,4,5])
    if verse == 1:
        return verse1()
    elif verse == 2:
        return verse2()
    elif verse == 3:
        return verse3()
    elif verse == 4:
        return verse4()
    else:
        return verse5()

for n in range(4):
        print(make_verse())
