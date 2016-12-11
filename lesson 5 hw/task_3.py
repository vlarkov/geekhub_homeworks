# Дано натуральное число N. Выведите все его цифры по одной, в обратном
# порядке, разделяя их пробелами или новыми строками. При решении этой
# задачи нельзя использовать строки, списки, массивы и циклы(разрешена
# только рекурсия и целочисленная арифметика).

# User's input
N = int(input("Please enter an integer number: "))


# Function for reverse user's input
def reverse(n):
    if n < 10:
        return str(n)
    else:
        return str(n % 10) + " " + str(reverse(n // 10))


print(reverse(N))
