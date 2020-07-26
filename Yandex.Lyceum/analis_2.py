words_frequency = {}
all_words = []
decrease_frequency = []
strings_quantity = int(input())
for i in range(strings_quantity):
    new_string = input()
    new_string = new_string.replace('.', '')
    new_string = new_string.replace(',', '')
    new_string = new_string.replace('!', '')
    new_string = new_string.replace('?', '')
    new_string = new_string.replace(':', '')
    new_string = new_string.replace(';', '')
    all_words.append(new_string.split())
all_words = sum(all_words, [])

for j in range(len(all_words)):
    all_words[j] = all_words[j].lower()
    words_frequency[all_words[j]] = words_frequency.get(all_words[j], 0) + 1

keys = list(words_frequency.keys())

keys.sort(
    key=lambda x: words_frequency[x] * 99999999999999999 - sum(
        [(ord(x[i]) - 1071) * (33 ** (10 - i)) for i in range(len(x))]), 
    reverse=True)
# for i in range(len(keys) - 1):
#     for j in range(len(keys) - i - 1):
#         key = keys[j]
#         next_key = keys[j + 1]
#         if words_frequency[key] < words_frequency[next_key] or \
#                 (words_frequency[key] == words_frequency[next_key] and keys[j] > keys[j + 1]):
#             keys[j], keys[j + 1] = keys[j + 1], keys[j]

for k in range(len(keys)):
    print(keys[k].capitalize())
