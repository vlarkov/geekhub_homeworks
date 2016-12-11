# Дано слово, состоящее только из строчных латинских букв.
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.
# При решении этой задачи нельзя пользоваться циклами или срезами с шагом, отличным от 1.

# User's input
user_input = ""
while len(user_input) < 1:
    user_input = input("Please enter any word you want: ")


# Function for palindrome check
def is_palindrome(checking_string):
    if len(checking_string) == 1:
        return "YES"
    else:
        if checking_string[0] == checking_string[-1]:
            if len(checking_string) == 2:
                return "YES"
            return is_palindrome(checking_string[1:len(checking_string) - 1])
        else:
            return "NO"


print(is_palindrome(user_input))
