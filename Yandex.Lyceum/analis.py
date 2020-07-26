passwd = input().lower().replace(' ', '')
often_count_letter = 0
often_letter = None

for letter in passwd:
    count_letter = passwd.count(letter)
    if count_letter > often_count_letter or \
            (count_letter == often_count_letter and ord(letter) < ord(often_letter)):
        often_count_letter, often_letter = count_letter, letter

print(often_letter)
