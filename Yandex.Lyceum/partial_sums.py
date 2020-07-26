def partial_sums(*numbs):
    numbs = list(numbs)
    if numbs == []:
        return [0]   
    default = [0, numbs[0]]
    if len(numbs) == 1:
        return default

    result = []
    for i in range(2, len(numbs) + 1):
        result.append(sum(numbs[:i]))
    result = default + result
    return result
