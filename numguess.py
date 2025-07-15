import random
guess_number = random.randint(1, 10)

print("Guess a number between 1 and 10.")
print("You have 5 tries to guess the right number.")

for attempt in range(1, 6):
    guess = int(input(f"Try #{attempt}: "))

    if guess == guess_number:
        print("Correct! You guessed it.")
        break
    elif guess < guess_number:
        print("Too low.")
    else:
        print("Too high.")
else:
    print(f"Sorry, you're out of tries. The number was {guess_number}.")
