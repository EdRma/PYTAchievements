import random
word_list = ["schaap", "baard", "chocolade", "openbaar", "weiland", "strandhuis", "spook"]

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Raad een letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("dit heb je al geprobeerd", guess, "!")
            elif guess not in word:
                print(guess, "is niet in het woord :(")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("lekker bezig,", guess, "is in het woord!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("dit heb je al geprobeerd ", guess, "!")
            elif guess != word:
                print(guess, " is niet in het woord :(")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("verkeerde input")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("goed gedaan, je hebt het woord geraden!")
    else:
        print("sorry, je hebt het woord niet geraden. het woord was " + word + ". hopelijk heb je hem de volgende keer!")




def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[tries]

def main():
    word = get_word(word_list)
    play(word)
    while input("Nog een keer? (J/N) ").upper() == "J":
        word = get_word(word_list)
        play(word)

if __name__ == "__main__":
    main()