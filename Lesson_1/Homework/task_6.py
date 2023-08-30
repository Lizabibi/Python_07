"""Вы пользуетесь общественным транспортом? Вероятно,
вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета."""

# Вариант 1 - Original
n = 385916
n1 = n // 100000
n2 = (n % 100000) // 10000
n3 = (n % 10000) // 1000
n4 = (n % 1000) // 100
n5 = (n % 100) // 10
n6 = n % 10
if n1 + n2 + n3 == n4 + n5 + n6:
    print('yes')
else:
    print('no')


# Вариант 2 - Original Можете использовать решение через нумерацию строк
n = 385916
n = str(385916)
if int(n[0]) + int(n[1]) + int(n[2]) == int(n[3]) + int(n[4]) + int(n[5]):
    print('yes')
else:
    print('no')


# Вариант 3
n = input()
if sum(int(i) for i in n[:3]) == sum(int(i) for i in n[3:]):
    print('Да')
else:
    print('Нет')


# Вариант 4
n = input()
if sum(map(int, n[:3])) == sum(map(int, n[3:])):
    print('Да')
else:
    print('Нет')
