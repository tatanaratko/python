friends_count = int(input())
phone_book = {}
for vasia_friend in range(friends_count):
    friend = input().split()
    if friend[0] in phone_book.keys():
        phone_book[friend[0]] += (str(friend[1]) + ' ').split()
    else:
        phone_book[friend[0]] = friend[1]
print(phone_book)
want_call = int(input())
for vasia_friend in range(want_call):
    friend_name = input()
    friend_number = phone_book.get(friend_name, 'Нет в телефонной книге')
    print(friend_number)