from math import sqrt


def discriminant(a, b, c):
    disc = b ** 2 - 4 * a * c
    return disc


def larger_root(p, q):
    disc = discriminant(1, p, q)
    x1 = (- p + sqrt(disc)) / 2
    return x1


def smaller_root(p, q):
    disc = discriminant(1, p, q)
    x2 = (- p - sqrt(disc)) / 2
    return x2


def main():
    p, q = float(input()), float(input())
    print(discriminant(1, p, q))
    print(smaller_root(p, q), larger_root(p, q))
