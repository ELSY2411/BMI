import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "code", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    chosen_word = choose_word()
    guessed_letters = []
    max_attempts = 6
    attempts = 0

    print("Welcome to Hangman!")
    print(display_word(chosen_word, guessed_letters))

    while "_" in display_word(chosen_word, guessed_letters) and attempts < max_attempts:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in chosen_word:
            attempts += 1
            print(f"Incorrect guess! Attempts left: {max_attempts - attempts}")
        else:
            print("Correct guess!")

        print(display_word(chosen_word, guessed_letters))

    if "_" not in display_word(chosen_word, guessed_letters):
        print("Congratulations! You guessed the word.")
    else:
        print(f"Sorry, you ran out of attempts. The word was {chosen_word}.")

if __name__ == "__main__":
    hangman()