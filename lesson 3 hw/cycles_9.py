"""9. Пользователь вводит английскую букву. Вывести следующие три по алфавиту. Если алфавит закончился, то
вывести циклично с начала алфавита (то есть если введена z , нужно вывести a b c ). Выводить только
строчные (маленькие) буквы. Учесть, что пользователь может ввести заглавную букву."""

import string

user_input = input().lower()

alphabet = string.ascii_lowercase
for i in range(len(alphabet)):
    if user_input == alphabet[i]:
        if 0 <= i <= len(alphabet) - 4:
            for j in range(i + 1, i + 4):
                print(alphabet[j], end=' ')
            break
        elif len(alphabet) - 3 <= i < len(alphabet):
            for j in range(i - len(alphabet) + 1, i - len(alphabet) + 4):
                print(alphabet[j], end=' ')
            break
