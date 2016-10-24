print("Enter a, b, l, N:")
a = int(input())
b = int(input())
l = int(input())
N = int(input())

L = (l * 2) + (a * ((N * 2) - 1)) + ((N - 1) * 2) * b

print("You need: " + str(L))
