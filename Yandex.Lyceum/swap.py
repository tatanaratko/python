def swap(first, second):
    if first == second:
        return
    first_swap = first[:]
    second_swap = second[:]
    first.clear()
    second.clear()

    for i in range(len(second_swap)):
        first.append(second_swap[i])

    for j in range(len(first_swap)):
        second.append(first_swap[j])
