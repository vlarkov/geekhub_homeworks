# Задание 1
# Дана строка.
# Вывести третий символ этой строки.

my_str = input()
print(my_str[2])

# Вывести предпоследний символ этой строки.

print(my_str[-2])

# Вывести первые пять символов этой строки.

print(my_str[0:5])

# Вывести всю строку, кроме последних двух символов.

print(my_str[:-2])

# Вывести длину данной строки.

print(len(my_str))

# Вывести все символы с четными индексами.*

print(my_str[::2])

# Вывести все символы с нечетными индексами.*

print(my_str[1::2])

# Вывести все символы в обратном порядке.*

print(my_str[::-1])

# Вывести все символы строки через один в обратном порядке, начиная с последнего.*

print(my_str[::-2])