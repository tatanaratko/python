PI = 3.14159


def circle_length(radius):
    length = 2 * radius * PI
    return length


def circle_area(radius):
    area = radius ** 2 * PI
    return area


def main():
    radius = float(input())
    print(circle_length(radius))
    print(circle_area(radius))
