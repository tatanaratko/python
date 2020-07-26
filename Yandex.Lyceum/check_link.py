phrase_words = input().split()
counted_words = {}
result_string = ''
for word in phrase_words:
    counted_words[word] = counted_words.get(word, 0) + 1
    result_string += str(counted_words[word]) + ' '
print(result_string)
