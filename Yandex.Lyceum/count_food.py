
def count_food(days):
    count = 0
    for i in range(len(days)):
        count += daily_food[days[i] - 1]
    return(count)
    
daily_food = []