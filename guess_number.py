num = 8
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < num:
        print("Too low! Try again.")
    elif guess > num:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number:", num)
        break