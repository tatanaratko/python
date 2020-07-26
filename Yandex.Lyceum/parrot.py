to_print = []


def parrot(phrase):
    if phrase in to_print:
        print(phrase)
    else:
        to_print.append(phrase)
