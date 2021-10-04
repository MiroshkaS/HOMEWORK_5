w = int(input("Введите ширину: "))

for i in range(w):
    if i<=w/2:
        for j in range(i):
            print('', end=' ')
        for j in range(w - i * 2):
            print('*', end='')
        for j in range(i):
            print('', end=' ')
    else:
        for j in range(w - 1 -i):
            print('', end=' ')
        for j in range(w - (w -1 -i)*2):
            print('*', end='')
        for j in range(w - 1 -i):
            print('', end=' ')
    print()