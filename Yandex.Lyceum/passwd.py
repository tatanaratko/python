profile_info = input()
profile_count = 0
while profile_info != '':
    profile_info = profile_info.split(':')
    name = profile_info[5].split(',')
    profile_count += 1

passwds = input().split(';')

for i in range(profile_count):
    if profile_info[2] == passwds[i]:
        print('To:', profile_info[1], set='')
        print(profile_info[5], 'ваш пароль слишком простой, смените его.', sep='')

