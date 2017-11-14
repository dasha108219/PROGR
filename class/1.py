f = open("new.txt", encoding = "utf-8") 
s = f.read()
f.close()
print(s)
print(f.closed)

with open("new.txt", encoding = 'utf-8') as f:
    s=f.read()
print(f.closed)
print(s)
          
  
