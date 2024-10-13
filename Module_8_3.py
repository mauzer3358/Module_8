class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

#    Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность.
    #    Возвращает True, если корректный, в других случаях выбрасывает исключение.Уровень доступа private.
    def __is_valid_vin(self,vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif vin_number>=1000000 and vin_number<10000000 :
            return True
        else:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')




#    Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность.
    #    Возвращает True, если корректный, в других случаях выбрасывает исключение.Уровень доступа private.

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers) == 6:
            return True
        else:
            raise IncorrectCarNumbers('Неверная длина номера')


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')