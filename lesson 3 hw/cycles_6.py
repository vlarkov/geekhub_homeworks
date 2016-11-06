# 6. Выведите на экран таблицу умножения для чисел от 1 до 10.

for i in range(1, 11):
    for j in range(1, 11):
        print(str(i) + " * " + str(j) + " = " + str(i * j))
    print()
