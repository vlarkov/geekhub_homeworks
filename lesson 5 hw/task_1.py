# Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки,
# или слово NO в противном случае. Операцией возведения в степень пользоваться нельзя.

# User's input
N = int(input("Please enter an integer number: "))


# This function finds out if the user's input is the power of 2
def power_of_two(n):
    p = 1
    while p < n:
        p *= 2
        if p == n:
            print("YES")
            break
    else:
        print("NO")

power_of_two(N)
