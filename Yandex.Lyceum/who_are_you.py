def who_are_you_and_hello():
    name = input()
    while name.capitalize() != name or len(name.split()) > 1 or name.isalpha() is not True:
        name = input()
    print(f'Привет, {name}!')
