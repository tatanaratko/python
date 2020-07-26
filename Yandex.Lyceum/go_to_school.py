def late(now, classes, bus):
    splited_now = now.split(':')
    splited_classes = classes.split(':')
    now = int(splited_now[0]) * 60 + int(splited_now[1])
    classes = int(splited_classes[0]) * 60 + int(splited_classes[1])
    time_to_run = classes - now
    stock = -1
    if time_to_run < 20:
        return 'Опоздание'
    else:
        for i in range(len(bus)):
            if bus[i] >= 5 and time_to_run >= bus[i] + 15:
                stock = bus[i] - 5
        if stock == -1:
            return 'Опоздание'
        else:
            return 'Выйти через ' + str(stock) + ' минут'
