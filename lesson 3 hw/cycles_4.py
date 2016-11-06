# 4. Найдите хотя бы одно натуральное число, которое делится на 11, а при делении на 2, 3, 4, ..., 10 дает в
# остатке 1.

i = 0
marker = True

while marker:
    if i % 11 == 0:
        for j in range(2, 11):
            if i % j != 1:
                i += 1
                break
            elif j == 10:
                marker = False
    else:
        i += 1
print(i)
