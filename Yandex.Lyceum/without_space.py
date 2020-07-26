string = input()
splited = string.strip().split(' ')

new_str = ''
for let in splited:
    let = let.strip().replace('\t', '')
    new_str += let
print(len(new_str))
