# -*- coding: utf-8 -*-

"""Main module."""
<<<<<<< HEAD


def gcd(a, b):
=======
def gcd(a , b):
>>>>>>> a4ad41312ce1d2053c5704e7f8876a1e2d5fdfa4
    while a != 0:
        a, b = b % a, a
    return b
