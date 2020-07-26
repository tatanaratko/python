from math import sqrt


def solve(*coefficients):
    if len(coefficients) == 3:
        if discriminant(*coefficients) < 0:
            return []
        disc = discriminant(*coefficients)
        x1 = larger_root(*coefficients)
        x2 = smaller_root(*coefficients)
        if x1 == x2:
            return [x1]
        else:
            return [x1, x2]
    elif len(coefficients) == 2:
        return [root(*coefficients)]
    elif len(coefficients) == 1 and coefficients[0] == 0:
        return ['all']
    elif len(coefficients) == 1 and coefficients[0] != 0:
        return []
    else:
        return None


def discriminant(a, b, c):
    disc = b ** 2 - 4 * a * c
    return disc


def root(b, c):
    x = - c / b
    return x


def larger_root(a, b, c):
    disc = discriminant(a, b, c)
    x1 = (- b + sqrt(disc)) / (2 * a)
    return x1


def smaller_root(a, b, c):
    disc = discriminant(a, b, c)
    x2 = (- b - sqrt(disc)) / (2 * a)
    return x2
