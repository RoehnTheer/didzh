import sys


def fibo(number):
    if number in (1, 2):
        return 1
    return fibo(number - 1) + fibo(number - 2)
mas = int(sys.argv[1])
print(fibo(mas))