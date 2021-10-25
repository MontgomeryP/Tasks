data = [23, 1, 95, 3, 8, 56, 38, 2, 9, 142, 51, 76, 5]


def median(data):
    list.sort(data)
    number_of_elements = len(data)

    if number_of_elements % 2 != 0:
        print(data[number_of_elements // 2])
    else:
        print((data[number_of_elements // 2] + (data[number_of_elements // 2 - 1]))/2)


median(data)


