import random

num = random.randint(1, 10)
print("Guess the number")

while True:
    guess = int(input("Enter your number: "))

    if guess < num:
        print("It is too low")
    elif guess > num:
        print("It is too high")
    else:
        print("Congrats! you guess the right.")