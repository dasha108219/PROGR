#def get_synonims(target):
#target = target.capitalize()
with open("syn.txt", encoding = 'utf - 8') as f:
    for line in f:
        line_split = line.split('#')
        if len(line_split) < 2:
            continue
        word = line_split[0]
        syns = line_split[1]
        syns = syns.strip()
        syns_list =syns.split(', ')
        if len(syns_list) == 1:
            print(word,'-', syns)

           # if word == target:
            #    syns = line_split[1]
             #   syns = syns.strip()
              #  syns_list =syns.split(', ')
               # return(syns_list)


#target = input()
#while target != "":
 #   print(get_synonims(target))
  #  target = input()
#while True:
 #   target =input()
  #  if target == '':
   #     break
    #print(get_synonims(target))
