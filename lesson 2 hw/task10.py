# Задание 10*
# Дана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h,
# а также все символы, находящиеся между ними.


my_str = input()
first = my_str[:my_str.find('h')]
last = my_str[my_str.rfind('h') + 1:]

print(first + last)
