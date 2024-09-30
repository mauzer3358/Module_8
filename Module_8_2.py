def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    res_cortege = 0

    for i in numbers:
        try:
            result += i

        except (TypeError):
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
        res_cortege = (result, incorrect_data)
    return res_cortege


def calculate_average(numbers):

    try:
        a = personal_sum(numbers)[0]

    except (TypeError):
        print('В numbers записан некорректный тип данных')
        return

    correct_data = 0
    try:
        for i in numbers:
            if type(i) == int:
                correct_data +=1
        avarage = a/correct_data
        return avarage

    except(ZeroDivisionError):
        return a



print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

