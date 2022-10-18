x = ['Philani', 20, 2.5]

for i in x:
    print(i)

x = 'PHILANI'

for i in x:
    print(i)

for i in range(10):
    print(i)

for i in range(11,21,1):
    print(i)

for i in range(20,10,-1):
    print(i)

for i in range(1,21):
    if(i%5!=0):
        print(i)
   
for j in range(4):
    for i in range(4): 
        print ("# ",end="")
    print()
    
for j in range(4):
    for i in range(j+1): 
        print ("# ",end="")
    print()

for j in range(4):
    for i in range(4-j): 
        print ("# ",end="")
    print()



