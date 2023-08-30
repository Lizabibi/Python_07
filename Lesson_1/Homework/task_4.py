""" Петя, Катя и Сережа делают из бумаги журавликов.
Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок, если известно,
что Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?"""

# Вариант 1 - Original
n = int(input())
n1 = n // 6
n2 = n // 6
n3 = (n // 6) * 4
print(n1, n3, n2)

# Вариант 2
"""
Находим x сразу, тем самым избегаем повторного деления на 6. 
Тут мы решаем уравнение:
1x + 1x + 2(1x + 1x) = 60
1x + 1x + 2x + 2x = 60
1x + 1x + 4x = 60
6x = 60

Поэтому и делим на 6.
"""
x = int(input()) // 6
n1 = n2 = x
n3 = x * 4
print(n1, n3, n2)
