# Guess a number between 1 - 100
# Respond with "too high" or "too low"
# Create a congratulations message when they guess the number correctly
# keep track of how many attempts it took to guess the number correctly


import random
# Generates a random number
secret_number = random.randint(1, 100)
attempts = 0

while True:
    # Prompt the user to guess the number
    guess =  int(input("Guess a number between 1 and 100: "))
    attempts += 1

    # check if the guess is too high, too low or if it is correct
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high")
    else:
        print(f"Congrats! You guessed the correct number in {attempts} attempts.")
        break
    


