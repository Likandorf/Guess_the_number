import random
from replit import clear

def play_game():
  game_on = True
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100.")
  number = random.choice(range(1, 101))
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    attempts = 10
  elif difficulty == "hard":
    attempts = 5

  while game_on:
    print(f"You have {attempts} attempts remaining.")
    guess = int(input("Make a guess: "))
    if attempts == 0:
      print("You have ran out of attempts.")
      print("You lose.")
      game_on = False
    elif guess > number:
      print("Too high.")
      attempts -= 1
    elif guess < number:
      print("Too low.")
      attempts -= 1
    elif guess == number:
      print("You guessed correctly.")
      print("You win!")
      game_on = False

while input("Do you want to try guessing the number? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
  
  