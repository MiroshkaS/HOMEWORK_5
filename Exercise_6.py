from random import randint
x=[]
for i in range(4):
    x.append(randint(0,100))
print(x)
new_list=x+[i*2 for i in x]
print(new_list)