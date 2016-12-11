# Дано натуральное число N. Вычислите сумму его цифр.
# Нельзя использовать строки, списки, массивы и циклы.

# User's input
N = int(input("Please enter an integer number: "))


# This function finds out the sum of number in user's input
def sum_finder(n):
    if n < 10:
        return n
    else:
        return n % 10 + int(sum_finder(n / 10))


print(sum_finder(N))
