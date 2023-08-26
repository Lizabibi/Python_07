

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

restult = fact(4)
print(restult)

fact(4)
--> 4 * 6
    4 * fact(3)
        --> 3 * (2 * 1) = 6
        3 * fact(2)
            --> 2 * 1 = 2
            2 * fact(1)
                --> 1