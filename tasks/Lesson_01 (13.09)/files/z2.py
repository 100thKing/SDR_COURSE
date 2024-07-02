import random as rn

random_numbers = []
for _ in range(1024):
    number = rn.randint(-1000, 1000)
    random_numbers.append(number)

random_numbers.sort()

# удаление отриц чисел
positive_numbers = []
for number in random_numbers:
    if number >= 0:
        positive_numbers.append(number)
#print(positive_numbers)



