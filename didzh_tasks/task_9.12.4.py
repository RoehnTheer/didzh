def is_prime_number(number: int) -> bool:
    """Returns True, if `number` is prime, otherwise returns False"""
    k = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            k = k + 1
    if k == 0:
        return True

def get_next_prime_number(number: int) -> int:
    """Returns next primer number after `number`"""
    k = number + 1
    while is_prime_number(k) is not True:
        k = k + 1
    return k

#Другой вариант через теорему Вильсона
# import math

# def is_prime_number(number: int) -> bool:
#     """Returns True, if `number` is prime, otherwise returns False"""
#     if (math.factorial(number - 1) + 1) % number == 0:
#         return True
#     else:
#         return False


# def get_next_prime_number(number: int) -> int:
#     """Returns next primer number after `number`"""
#     number += 1
#     while not is_prime_number(number):
#         number += 1
#     else:
#         return number