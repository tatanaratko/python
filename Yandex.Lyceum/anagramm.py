quantity_words = int(input())
anagramms = {}
for word in range(quantity_words):
    new_word = input().lower()
    key = str(sorted(new_word))
    if key in anagramms:
        anagramms[key].add(new_word)
    else:
        anagramms[key] = set()
        anagramms[key].add(new_word)

anagramms_list = list(map(lambda x: list(x), list(anagramms.values())))
anagramms_list = sorted(anagramms_list, key=lambda x: " ".join(x))

for a in anagramms_list:
    if len(a) > 1:
        print(*sorted(a))
