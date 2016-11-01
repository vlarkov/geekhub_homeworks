"""
Задача 3
Шоколадка имеет вид прямоугольника, разделенного на n×m долек. Шоколадку можно один раз разломить по
прямой на две части. Определите, можно ли таким образом отломить от шоколадки часть, состоящую ровно из k
долек. Программа получает на вход три числа: n, m, k и должна вывести YES или NO.
4
2
6
YES

2
10
7

NO

5
7
1

NO

7
4
21

YES

5
12
100

NO

6
6
6

YES

6
6
35

NO

6
6
37

NO

7
1
99

NO

300
100
3000

YES

256
124
4069

NO

348
41
6183

NO

387
13
2709

YES

13
387
2709

YES

1
1
2

NO
"""

n = int(input())
m = int(input())
k = int(input())

if k == n or k == m:
    print("YES")
elif k < m and k < n:
    print("NO")
elif k > m and k > n:
    if k > n * m:
        print("NO")
    elif k < n * m and k % m == 0 or k % n == 0:
        print("YES")
    else:
        print("NO")
elif n < k < m:
    if k % n == 0:
        print("YES")
    else:
        print("NO")
elif m < k < n:
    if k % m == 0:
        print("YES")
    else:
        print("NO")
