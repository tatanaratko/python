def ask_password():
    count_try = 0
    true_passwd = 'password'
    for i in range(3):
        passwd = input()
        if passwd == true_passwd:
            print('Пароль принят')
            break
        elif count_try == 2:
            print('В доступе отказано')
        elif count_try < 2:
            count_try += 1
