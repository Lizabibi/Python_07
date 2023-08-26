"""37. Дано натуральное число *N* и 
последовательность из *N* элементов. 
Требуется вывести эту последовательность в обратном порядке.

***Примечание.*** В программе запрещается объявлять массивы 
и использовать циклы (даже для ввода и вывода)."""


def sequence_printing(n):
    if n == 0:  # Выход из рекурсии
        return ''
    k = int(input())
    # Вычетаем -1, иначе не достигнем базового случая
    return sequence_printing(n - 1) + f' {k}'


print(sequence_printing(4))
