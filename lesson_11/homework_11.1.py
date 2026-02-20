list_of_numbers_str = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def sum_for_elements(list):
    result_list = []
    for i in list:
        element_str = i.split(",")
        element_int = []
        try:
            for j in element_str:
                element_int.append(int(j))
        except ValueError:
            result_list.append('"Не можу це зробити"')
            continue
        result = 0
        for k in element_int:
            result += k
        result_list.append(result)
    print(*result_list, sep=', ')

sum_for_elements(list_of_numbers_str)











