# 5. Вывести английский алфавит по 5 букв в строке.
import string

alphabet = list(string.ascii_lowercase)
for i in range(len(alphabet)):
    if i % 5 == 0:
        print()
        print(alphabet[i], end='')
    else:
        print(alphabet[i], end='')
