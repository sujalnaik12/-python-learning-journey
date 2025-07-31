secret_number = 7
guess = int(input("Guess the secret number (between 1 and 10): "))
if (guess == secret_number):
  print("You guessed it right!")
else:
  print("Wrong guess! Try again.")
