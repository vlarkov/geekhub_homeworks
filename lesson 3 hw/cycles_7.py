"""7. Начав тренировки, лыжник в первый день пробежал 10 км. Каждый следующий день он увеличивал пробег на
10% от пробега предыдущего дня. Определите: а) пробег лыжника за второй, третий, ..., десятый день
тренировок; б) какой суммарный путь он пробежал за первые 7 дней тренировок. в) суммарный путь за n дней
тренировок; г) в какой день ему следует прекратить увеличивать пробег, если он не должен превышать 80 км?"""

i = 10
ni = 10
kilos_per_n_days = 10
counter = 0

total_kilo = []
kilos_per_week = 0

total_kilo.append(i)
for j in range(2, 11):
    i += 0.1 * i
    total_kilo.append(i)
    print("day: " + str(j))
    print("kilometrage: " + str(i))

for k in range(1, 8):
    kilos_per_week += total_kilo[k - 1]
print()
print("kilometrage per week: " + str(kilos_per_week))

n = int(input())
for l in range(2, n + 1):
    ni += 0.1 * ni
    kilos_per_n_days += ni

print()
print("kilometrage per " + str(n) + " days: " + str(kilos_per_n_days))

for z in range(len(total_kilo)):
    if counter < 80:
        counter += total_kilo[z]
    else:
        print("stop on " + str(z - 1) + "th day")
        break
