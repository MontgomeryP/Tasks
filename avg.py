name = [4, 7, 19, 23, 5, 9]
number_of_elements = len(name)
summa = 0
for i in name:
    summa = summa + i

avg = summa/number_of_elements
print(avg)

if sum(name) / len(name) == avg:
    print("УРА!")