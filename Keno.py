import random
import time


# Creates 20 Random numbers between 1 and 80
def CreateNumbers():
    numbers = []
    while len(numbers) is not 20:
        random_number = random.randint(1,80)
        if(random_number in numbers):
            pass
        else:
            numbers.append(random_number)
    return numbers


# Displays the Numbers
def ShowNumbers(numbers):
    for num in range(len(numbers)):
        time.sleep(1)
        print(numbers[num])


# Check User Numbers With The List
def CheckNumbers(user_numbers,numbers):
    score = 0
    for num in range(len(user_numbers)):
        if(user_numbers[num] in numbers):
            score = score + 1
    return score
        





    







