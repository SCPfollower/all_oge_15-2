#Вариант 80
a = int(input("Введите число цифр: "))
b = []
for i in range(a):
    d = int(input("Nomer: "))
    if d % 3 == 0:
        b.append(d)
c = min(b)
print(c)
#Вариант 40 и почти 100
import math
a = int(input("Ввеите количество цифр: \n"))
b = []
c = []
for i in range(a):
    b = [int(input("Введите цифру: "))]
    for n in b:
        if n % 6 == 0:
            c.append(n)
            b.remove(n)
s = math.fsum(c)
print(s)
#Вариант 621
a = True
b = 0
while a != 0:
    a = int(input("Введите целое число: "))
    if (a % 6 == 0) and (a % 10 == 4):
        b += a
print(b)
#Вариант 1071
a = int(input("Число участников: "))
b = 0
c = False
d = []
for i in range(a):
    b = int(input("Введите число правильных ответов ученика: "))
    if b == 0:
        c = True
    d.append(b)
mx = max(d)
print(mx)
if c == True:
    print("YES")
else:
    print("NO")
#Вариант 1233
a = True
b = 0
while a != 0:
    a = int(input("Введите число: "))
    if (99 < a < 1000) and (a % 4 == 0):
        b += 1
print(b)
#Вариант 1253
import math
a = 1
b = 0
c = []
d = -1
while a != 0:
    a = int(input("Введите число: "))
    if a % 8 == 0:
        c.append(a)
        d += 1
if d > 0:
    b = float(math.fsum(c) / d) #Можно сделать через переменную, кратную 0 и послед. прибавление к ней переменной "а", если подходит по условию
    print((round(b, 1)))
else:
    print("NO")
#Вариант 4609
a = True
b = 0
while a != 0:
    a = int(input("Num: "))
    print(b)
    if (a % 5 == 0) or (a % 9 == 0):
        b += 1
    if a == 0:
        b -= 1 #Тут переменная b после введения цифры 0 проходит по кратности 5 или 9, и прибавляется однерка. Поэтому приходится либо ставить вначале b = -1, либо отнимать вконце
print(b)
#Вариант 5085
a = int(input("A = "))
b = int(input("B = "))
c = b - a
d = 0
if b % 2 != 0:
    for i in range(-1, c):
        if i % 2 == 0:
            d += 1
else:
    d = 1
    for n in range(c):
        if n % 2 == 0:
            d += 1
print(d)
#Вариант 18254 (что так много)
import math
a = True
b = []
c = 0
d = 0
while a != 0:
    a = int(input("Number: "))
    if (9 < a < 99):
        b.append(a)
        c += 1
if c == 0:
    print("NO")
else:
    d = float(math.fsum(b) / c)
    print(d)
#Неизвестный вариант
a = True
b = 0 #Не обязательно, только для красоты внизу
c = []
d = 0 #Не обязательно, только для красоты внизу
while a != 0:
    a = int(input("Номер: "))
    if a != 0:
        c.append(a)
c.sort()
print(c)
b = c[-1] + c[-2]
d = c[0] + c[1]
print("Сумма наибольших цифр = " + str(b) + ". Сумма наименьших = " + str(d))
#Варинат 18260
a = True
b = 0
d = 0
while a != 0:
    a = int(input("Номер: "))
    if a % 8 == 0:
        b += a
        d += 1
if d != 1:
    print(round(b/(d-1),1)) #Тут как в варианте 4609
else:
    print("NO")
#Вариант 4637
a = int(input("Kolichestvo "))
c = 0
an = False
for i in range(a):
    b = int(input("Ocenka: "))
    if b < 5:
        c += 1
    if b == 10:
        an = True
print(c)
if an == True:
    print("YES")
else:
    print("NO")