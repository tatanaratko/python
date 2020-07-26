import pymorphy2

# MorphAnalyzer - класс
morph = pymorphy2.MorphAnalyzer()
# Метод парс принимает слово для анализа
result = morph.parse('Ленка')
print(len(result))
print(result)

my_mor = pymorphy2.MorphAnalyzer()
res = my_mor.parse('программирование')[0]
# проверка на существительное 
print('NOUN' in res.tag)
# падеж
print('accs' in res.tag)
# сущ в им падеже
print({'NOUN', 'nomn'} in res.tag)

