# 2. Вывести на экран ряд чисел 1001, 1004, 1007, ... 1025.

n = 1001
out = ''
while n <= 1025:
    out += str(n) + ", "
    n += 3

print(out[:len(out) - 2] + ".")
