def month_name(month_number, month_len):
    ru_month = ['январь', 'февраль', 'март',
                'апрель', 'май', 'июнь',
                'июль', 'август', 'сентябрь',
                'октябрь', 'ноябрь', 'декабрь']

    en_month = ['january', 'february', 'march',
                'april', 'may', 'june',
                'july', 'august', 'september',
                'october', 'november', 'december']

    return ru_month[month_number - 1] if month_len == 'ru' else \
        en_month[month_number - 1]
