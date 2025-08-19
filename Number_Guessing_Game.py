import random

def number_guessing_game():
    # 1. Random number generate karo
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("🎲 Welcome to Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.\n")

    # 2. Loop for attempts
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            # 3. Check guess
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("📉 Too Low! Try again.")
            else:
                print("📈 Too High! Try again.")
        
        except ValueError:
            print("⚠️ Please enter a valid number.")
        
        # 4. If attempts over
        if attempts == max_attempts:
            print(f"\n❌ Sorry, you've used all {max_attempts} attempts.")
            print(f"The correct number was: {secret_number}")

# Run the game
number_guessing_game()
