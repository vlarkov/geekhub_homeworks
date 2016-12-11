# Написать программу для шифрования и дешифрования заданного текста с помощью шифра Цезаря.
# Текст нужно вводить с клавиатуры. Шифрование и дешифрование должно быть реализовано в виде функций.
# При запуске программа должна спрашивать, что нужно сделать, и вызывать соответствующую функцию.


# User's option
option = ""
while option != 'e' and option != 'd':
    option = input("Press e to encode and d to decode: ")

# User's input
user_input = ""
while len(user_input) < 1:
    user_input = input("Please enter any word you want: ")


# Function for encode user's input
def encode_caesar(string_for_encoding):
    encoded_string = ""
    for i in range(len(string_for_encoding)):
        c = string_for_encoding[i]
        if 'x' <= c <= 'z':
            c = chr(ord(c) - 23)
        elif 'X' <= c <= 'Z':
            c = chr(ord(c) - 23)
        elif 'a' <= c <= 'w':
            c = chr(ord(c) + 3)
        elif 'A' <= c <= 'W':
            c = chr(ord(c) + 3)
        encoded_string += c
    return encoded_string


# Function for decode user's input
def decode_caesar(string_for_decoding):
    decoded_string = ""
    for i in range(len(string_for_decoding)):
        c = string_for_decoding[i]
        if 'd' <= c <= 'z':
            c = chr(ord(c) - 3)
        elif 'D' <= c <= 'Z':
            c = chr(ord(c) - 3)
        elif 'a' <= c <= 'c':
            c = chr(ord(c) + 23)
        elif 'A' <= c <= 'C':
            c = chr(ord(c) + 23)
        decoded_string += c
    return decoded_string


if option == 'e':
    print(encode_caesar(user_input))
else:
    print(decode_caesar(user_input))
