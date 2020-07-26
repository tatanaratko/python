def average(values):
    if values == []:
        return 0
    mean = sum(values) / len(values)
    if sum(values) % len(values) == 0:
        return int(mean)
    else:
        return mean
