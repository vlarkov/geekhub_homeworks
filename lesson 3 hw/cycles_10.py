"""10. Сгенерировать пароль для пользователя. Требования: длина от 6 до 20 символов, должен быть ровно один
символ подчеркивания, хотя бы две заглавные буквы, не более 5 цифр. Любые две цифры подряд
недопустимы."""

from random import randint, shuffle
import string

pass_length = randint(6, 20)
lowercase = string.ascii_lowercase  # base of password
uppercase = string.ascii_uppercase
digits = string.digits
list_password = []
digits_counter = randint(0, 5)
upper_count = randint(2, int(pass_length / 2))  # uppercase letters in password
start_add_digit = randint(0, 1)  # add digits from 0th or 1st index
marker = True

# generate password
for i in range(pass_length):
    list_password.append(lowercase[randint(0, len(lowercase) - 1)])

# add uppercase letters
for j in range(len(list_password)):
    if upper_count > 0:
        list_password[j] = uppercase[randint(0, len(uppercase) - 1)]
        upper_count -= 1

# shuffle letters
shuffle(list_password)

# add digits
for k in range(start_add_digit, len(list_password), 2):
    if digits_counter > 0 and uppercase.count(list_password[k]) == 0:
        list_password[k] = digits[randint(0, len(digits) - 1)]
        digits_counter -= 1

# add "_"
while marker:
    temp = randint(0, pass_length - 1)
    if uppercase.count(list_password[temp]) == 0 and digits.count(list_password[temp]) == 0:
        list_password[temp] = "_"
        marker = False
print(''.join(list_password))
