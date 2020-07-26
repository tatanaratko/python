input_str = input()

rescue_types_dict = {}

while(input_str != ''):
    rescue_type, character = input_str.split(' - ')
    if character in rescue_types_dict:
        rescue_types_dict[character].append(rescue_type)
    else:
        # сразу делаем способы спастись списком
        rescue_types_dict[character] = [rescue_type]

    input_str = input()

for k in rescue_types_dict.keys():
    rescue_types_dict[k] = sorted(rescue_types_dict[k], reverse=True)

result_order = sorted(rescue_types_dict.keys())

for r in result_order:
    type_str = ', '.join(rescue_types_dict[r])
    result_str = f'{r}: {type_str}'
    print(result_str)