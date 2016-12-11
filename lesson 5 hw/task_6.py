# Написать программу для кодирования данного текста с помощью азбуки Морзе (текст нужно вводить с клавиатуры).

# User's input
user_input = ""
while len(user_input) < 1:
    user_input = input("Please enter any word or sentence you want: ")
    user_input = user_input.upper()

characters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И',
              'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С',
              'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ы',
              'Ь', 'Э', 'Ю', 'Я', '1', '2', '3', '4', '5',
              '6', '7', '8', '9', '0']

morse_code = ["*–", "–***", "*––", "––*",
              "–**", "*", "***–", "––**",
              "**", "*–––", "–*–", "*–**",
              "––", "–*", "–––", "*––*",
              "*–*", "***", "–", "**–",
              "**–*", "****", "–*–*",
              "–––*", "––––", "−−*−",
              "−*−−", "−**−", "**−**",
              "**−−", "*−*−", "*−−−−",
              "**−−−", "***−−", "****−",
              "*****", "−****", "−−***",
              "−−−**", "−−−−*", "−−−−−"]


# Function for encoding user's string into Morse code
def encode_morse(input_string):
    output = ""
    for i in range(len(input_string)):
        if input_string[i] != ' ':
            output += morse_code[characters.index(input_string[i])] + " "
    output = output[:len(output) - 1]
    return output


print(encode_morse(user_input))
