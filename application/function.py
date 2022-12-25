def obj_sort(letters, color):
    k, s, z = [], [], []
    result = []
    for i in range(len(letters)):
        if letters[i] == 'З' or letters[i] == 'з':
            z.append(letters[i])
        elif letters[i] == 'С' or letters[i] == 'с':
            s.append(letters[i])
        elif letters[i] == 'К' or letters[i] == 'к':
            k.append(letters[i])
        elif letters[i] == ' ' or letters[i] == '':
            pass
        else:
            print('Введены некорректные объекты')
    if color == 'КЗС' or color == 'кзс':
        result = k + z + s
    elif color == 'КСЗ' or color == 'ксз':
        result = k + s + z
    elif color == 'ЗСК' or color == 'зск':
        result = z + s + k
    elif color == 'ЗКС' or color == 'зкс':
        result = z + k + s
    elif color == 'СКЗ' or color == 'скз':
        result = s + k + z
    elif color == 'СЗК' or color == 'сзк':
        result = s + z + k
    else:
        print('Введён некорректный порядок сортировки')
    return result
