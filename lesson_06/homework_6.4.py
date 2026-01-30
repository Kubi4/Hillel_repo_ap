new_list = [x for x in range(1, 21)]

x = 0
for el in new_list:
    if el % 2 == 0:
        x += el
