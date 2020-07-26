import pymorphy2
import sys


verbs = ['видеть', 'увидеть', 'глядеть', 'примечать', 'узреть']
morph = pymorphy2.MorphAnalyzer()
count_verbs = 0
for words in sys.stdin.readlines():
    for word in words.split():
        res = morph.parse(word)[0].normal_form
        if res in verbs:
            count_verbs += 1
print(count_verbs)