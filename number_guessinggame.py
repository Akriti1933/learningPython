import random

number = random.randint(1,10)
attempt = 0

while attempt <= 3:
    user_guess = int(input("guess the number between 1 to 10:\n"))
    attempt +=1

if(user_guess > 10 or user_guess <0):
    print("please enter a valid number")
else:
    if(number == user_guess):
        print("congratulation.")
        
    elif user_guess< number:
        print("your guess is low,please guess the higher number")
    else:
        print("your guess is high, please guess the low number")
    