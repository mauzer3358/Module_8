def add_everything_up(a, b):
    try:
        sum = round(a +b,3)
        return sum

    except(TypeError):
        if (type(a) == int or type(a) == float) and type(b) == str:
            a = str(a)
        elif type(a)==str and (type(b) == int or type(b) == float):
            b = str(b)
        sum = a+b
        return sum

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))