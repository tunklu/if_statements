print('Блок 1.')
x = 38
print('Здравствуйте!')
if x < 0:
    print('Меньше нуля')
print('Досвидания!')
# Пример
print('Блок 2.')
a, b = 10 ,5
if a > b:
    print('a > b')
if a > b and a > 0:
    print('Успех!')
if (a > b) and (a > 0 or b < 1000):
    print('Успех!')
if 5 < b or b < 10:
    print('Успех!')
# Можно сравнивать всё
print('Блок 3.')
if '34' > '123':
    print('Успех!')
if '123' > '12':
    print('Успех!')
if [1, 2] > [1, 1]:
    print('Успех!')
# Нельзя сравнивать разные типы
print('Блок 4.')
try:
    if '6' > 5:
        print('Успех!')
except TypeError:
    print('Нельзя сравнивать разные типы!')
try:
    if [5, 6] > 5:
        print('Успех!')
except TypeError:
    print('Нельзя сравнивать разные типы!')
# Но
    if '6' != 5:
        print('Успех!')

