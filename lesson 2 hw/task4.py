# Задание 4

# Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Переставьте эти слова местами. Результат запишите в строку и выведите получившуюся строку.
# Задача должна быть решена без использования оператора if


my_str = "Hello World!"

first = my_str[:my_str.find(' ')]
second = my_str[my_str.find(' ') + 1:]

result = second + ' ' + first
print(result)
