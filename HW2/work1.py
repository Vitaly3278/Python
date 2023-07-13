# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

num = int(input('Введите число для перевода:> '))
ex = hex(num)
result = ''
hexer = 16
while num >= 1:
    res = num % hexer
    if hexer == 16:
        if res == 10:
            res = 'a'
        if res == 11:
            res = 'b'
        if res == 12:
            res = 'c'
        if res == 13:
            res = 'd'
        if res == 14:
            res = 'e'
        if res == 15:
            res = 'f'
    result += str(res)
    num = num // hexer


print(f'{result[::-1]} >>> {ex}')
