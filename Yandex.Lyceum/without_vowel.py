translated_text = ''


def translate(text):

    for symbol in text:
        global translated_text
        ru_vowels = ['у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю',
                     'У', 'Е', 'Ы', 'А', 'О', 'Э', 'Я', 'И', 'Ю']
        if symbol not in ru_vowels and symbol.isalpha() is True or \
                symbol == ' ':
            translated_text = str(translated_text) + symbol
    translated_text = translated_text.split()
    translated_text = ' '.join(translated_text)
    return translated_text
