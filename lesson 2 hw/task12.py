# Задание 12*

# Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.

my_str = "0123456789"
new_str = ''
i = 0
for i in range(len(my_str)):
    if i % 3 != 0:
        new_str += my_str[i]
print(new_str)
