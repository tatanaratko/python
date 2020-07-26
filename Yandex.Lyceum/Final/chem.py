def chemical_equation(before, after):
    before_unwrapped = []
    for i in range(len(before)):
        substance, count = before[i]
        if count == 1:
            before_unwrapped.append(substance)
        else:
            before_unwrapped.append(f'{count}{substance}')

    before_str = " + ".join(before_unwrapped)

    after_unwrapped = []
    for i in range(len(after)):
        substance, count = after[i]
        if count == 1:
            after_unwrapped.append(substance)
        else:
            after_unwrapped.append(f'{count}{substance}')

    after_str = " + ".join(after_unwrapped)

    return before_str + " -> " + after_str