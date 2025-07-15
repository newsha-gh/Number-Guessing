# Number-Guessing
Number Guessing Game
A simple command-line number guessing game built with Python.
Description
This is a classic number guessing game where the computer randomly selects a number between 1 and 10, and the player has 5 attempts to guess it correctly. The game provides feedback after each guess, telling the player whether their guess is too high, too low, or correct.
How to Play

Run the program
The game will prompt you to guess a number between 1 and 10
Enter your guess and press Enter
The game will tell you if your guess is:

Correct - You win!
Too low - Try a higher number
Too high - Try a lower number


You have 5 attempts to guess the correct number
If you don't guess correctly within 5 tries, the game reveals the answer

Requirements

Python 3.x

How to Run

Save the code to a file (e.g., guessing_game.py)
Open your terminal/command prompt
Navigate to the directory containing the file
Run the command:
bashpython guessing_game.py


Example Gameplay
Guess a number between 1 and 10.
You have 5 tries to guess the right number.
Try #1: 5
Too low.
Try #2: 8
Too high.
Try #3: 7
Correct! You guessed it.
Features

Random number generation between 1-10
Limited attempts (5 tries)
Immediate feedback on each guess
Clear win/lose conditions
Simple and intuitive interface

Code Structure
The game uses Python's built-in random module to generate a random number and implements a simple game loop with user input validation and feedback system.
License
This project is open source and available under the MIT License
