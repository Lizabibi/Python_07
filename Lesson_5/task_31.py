"""Последовательностью Фибоначчи называется последовательность 
чисел a0, a1, ..., an, ..., где 
a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи"""


# -----------------
# Решение с использованием for
def fib_for(n):
    a, b = 0, 1
    for _ in range(n):  # _ - так как переменная не используется
        a, b = b, a + b  # Обмен значениями
    return a

print(fib_for(50))


# -----------------
# Решение рекурсии с проблемами
def fib_1(n):  # Плохое имя
    if n == 0 or n == 1:  # А если передать 0?
        return 1 # Получаем 1, тогда нужно считать что последовательность начинается с 1
    return fib_1(n - 1) + fib_1(n - 2)

# print(fib_1(2))


# -----------------
# Решение через рекурсию без проблем, но 50 элемент найти не сможем)
def fib_2(n):
    if n <= 1:
        return n
    return fib_2(n - 1) + fib_2(n - 2)

print(fib_2(35))


# -----------------
# Добавим кэширование - решает проблему повторных вызовов рекурсии
cahce = {}
def fib_rec_cache(n):
    if n not in cahce:
        if n <= 1:
            cahce[n] = n
        else:
            cahce[n] = fib_rec_cache(n - 1) + fib_rec_cache(n - 2)
    return cahce[n]

print(fib_rec_cache(100))



cahce = {}
def fib_rec_cache(n):
    if n not in cahce:
        cahce[n] = n if n <= 1 else fib_rec_cache(n - 1) + fib_rec_cache(n - 2)
    return cahce[n]

print(fib_rec_cache(1))




def return_1(number):
    if number > 10:
        return 1
    else:
        return 0
    
def return_1(number):
    return 1 if number > 10 else 0

a = 20
print(return_1(a))
    
