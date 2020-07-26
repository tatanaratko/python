def take_large_banknotes(banknotes):
    big_banknotes = []
    for i in range(len(banknotes)):
        if banknotes[i] > 10:
            big_banknotes.append(banknotes[i])
    return big_banknotes
    