# Задание 7

# Дана строка. Замение в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.

my_str = input()

first = my_str[:my_str.find('h') + 1]
middle = my_str[my_str.find('h') + 1:my_str.rfind('h')]
last = my_str[my_str.rfind('h'):]

print(first + middle.replace('h', 'H') + last)
