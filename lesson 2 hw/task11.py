# Задание 11*

# Дана строка, в которой буква h встречается как минимум два раза.
# Разверните последовательность символов, заключенную между
# первым и последнием появлением буквы h, в противоположном порядке.

my_str = input()
first = my_str[:my_str.find('h') + 1]
middle = my_str[my_str.find('h') + 1:my_str.rfind('h')]
last = my_str[my_str.rfind('h'):]

result = first + middle[::-1] + last

print(result)
