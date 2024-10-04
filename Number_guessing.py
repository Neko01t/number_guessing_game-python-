import random

num = random.randrange(1, 10)
print("\n" + "="*40)
print("🎲 WELCOME TO THE NUMBER GUESSING GAME 🎲".center(40))
print("="*40 + "\n")
print("I'm thinking of a number between 1 and 10. Can you guess it? 🤔")
chances = 7
guesses = 0
guess = 0

while guesses != chances:
    guess = int(input("\n🔢 Enter your guess: "))
    guesses += 1
    
    if guess == num:

        print("\n" + "="*40)
        print("🎉 CONGRATULATIONS! YOU'VE GUESSED THE NUMBER! 🎉".center(40))
        print(f"The correct number was {num}. You guessed it in {guesses} tries.".center(40))
        print("="*40 + "\n")

        break
    elif guess < num:
        print("⬆️ Your guess is too low! Try again.".center(40))
    elif guess > num:
        print("⬇️ Your guess is too high! Try again.".center(40))
    
if guess != num:
    print("\n" + "="*40)
    print("😔 OOPS! YOU'VE USED ALL YOUR CHANCES!".center(40))
    print(f"The correct number was {num}. Better luck next time! 🍀".center(40))
    print("="*40 + "\n")