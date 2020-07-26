word_coordinates = input().split()
words = input().split()
phrase = ''
for i in range(len(word_coordinates)):
    word_coordinate = int(word_coordinates[i]) - 1
    word_for_phrase = words[word_coordinate]
    phrase += word_for_phrase + ' '

print(phrase.capitalize())
