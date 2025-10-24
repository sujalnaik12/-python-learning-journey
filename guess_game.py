import random

print("WELCOME TO THE NUMBER GUESS GAME!")
print("I'm thinking of a number between 1 and 100.")

# generating random number
secret_number = random.randint(1, 100)

# number of attemps
attempts = 0

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
