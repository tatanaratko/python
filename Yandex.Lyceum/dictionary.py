words_count = int(input())
dictionary = {}
for word in range(words_count):
    word_with_desc = input().split()
    description = ' '.join(word_with_desc[1:])
    dictionary[word_with_desc[0]] = description

check_count = int(input())
for dict_word in range(check_count):
    mamas_word = input()
    desc_to_print = dictionary.get(mamas_word, 'Нет в словаре')
