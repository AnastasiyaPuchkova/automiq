letters = input('Введите объекты, каждый из которых помечен одним из 3х цветов: красный(К), зелёный(З) и синий(С): ')
color = input('Ввведите порядок сортировки цветов в порядке возрастания(#ЗСК = З<С<К): ')


def obj_sort(letters, color):  # Функция разделяет входную строку и записывает в отдельные списки определенные символы
    k, s, z = [], [], []
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
    if color == 'КЗС' or color == 'кзс':  # На выходе: соединяем всё в нужном порядке
        result = k + z + s
        print('Упорядоченный набор объектов: ', result)
    elif color == 'КСЗ' or color == 'ксз':
        result = k + s + z
        print('Упорядоченный набор объектов: ', result)
    elif color == 'ЗСК' or color == 'зск':
        result = z + s + k
        print('Упорядоченный набор объектов: ', result)
    elif color == 'ЗКС' or color == 'зкс':
        result = z + k + s
        print('Упорядоченный набор объектов: ', result)
    elif color == 'СКЗ' or color == 'скз':
        result = s + k + z
        print('Упорядоченный набор объектов: ', result)
    elif color == 'СЗК' or color == 'сзк':
        result = s + z + k
        print('Упорядоченный набор объектов: ', result)
    else:
        print('Введён некорректный порядок сортировки')


obj_sort(letters, color)
