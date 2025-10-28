import random

print("WELCOME TO THE NUMBER GUESS GAME!")

difficulty = input("Choose a difficulty level (easy/medium/hard): ").lower()

if difficulty == 'easy':
  max_number = 10
elif difficulty == 'hard':
  max_number = 1000
else:
  max_number = 100


# generating random number
secret_number = random.randint(1, max_number)

# number of attemps
attempts = 0

print(f"I'm thinking of a number between 1 and {max_number}.")

while True:
  # taking input from user
  guess = int(input("Enter your guess:  "))
  attempts += 1

  if guess < secret_number:
    print("Too low! Try again.")
  elif guess > secret_number:
    print(" Too high! Try again.")
  else:
    print(f"Correct! The secret number was {secret_number}.")
    print(f"You guessed it in {attempts} attempts.")
    break
