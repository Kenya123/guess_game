import random
from pyfiglet import Figlet
custom_fig = Figlet(font = "doom")
print(custom_fig.renderText("Guess!!"))
 
print("Welcome to the guessing game!")
print("Guess a number between 1 and 10")
print("Type exit if you'd like to leave the game")
random_number = random.randint(1, 10)
guess = 0 
count = 0
while guess != random_number and guess != "exit": 
 guess = input("Enter your guess: ")
 if guess == str(random_number):
  guess = guess
  count += 1
  print("You guessed correctly in: " + str(count) + " guesses")
  break;
 elif guess == "exit":
  print("Goodbye")
  break;
 elif guess > str(random_number):
  guess = guess
  count += 1
  print("Too high")
 elif guess < str(random_number):
  count += 1
  guess = guess
  print("Too low")
 
