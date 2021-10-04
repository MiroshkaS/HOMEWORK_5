from random import randint
x=[]
for i in range(12):
    x.append(randint(7500, 15000))
print(x)
zp=round(sum(x)/len(x),2)
print(zp)