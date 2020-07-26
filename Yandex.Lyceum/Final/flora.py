input_str = input()

encyclopedia = {}

while('//' in input_str):
    form, place, life_type = input_str.split(' // ')
    out_str = f'{form} ({life_type});'
    if place in encyclopedia:
        encyclopedia[place].append(out_str)
    else:
        encyclopedia[place] = [out_str]
    input_str = input()

result_list = sorted(encyclopedia[input_str], reverse=True)
print(*result_list, sep='\n')