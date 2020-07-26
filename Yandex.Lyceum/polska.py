symbols = input().split()
digits = []
for symbol in range(len(symbols)):
    sym = symbols[symbol]
    if sym.isdigit() or (sym[0] == '-' and len(sym) > 1):
        digits.append(sym)
    elif len(digits) > 1:
        digit2 = digits.pop()
        digit1 = digits.pop()
        operation_str = str(digit1) + str(sym) + str(digit2)
        operation_result = eval(operation_str)
        digits.append(operation_result)

print(digits[0])
