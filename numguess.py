import random
numberguess=int(input("Enter a number between 1 and 10: "))
result=random.randint(0,10)
if result == numberguess:
    print("Correct! You guessed it.")
else:
    print(f"Wrong. The correct number was {result}.")