import random
woord_lijst = ["schaap", "baard", "chocolade", "openbaar", "weiland", "strandhuis", "spook"]

def get_word(woord_lijst):
    woord = random.choice(woord_lijst)
    return woord.upper()


def play(woord):
    woord_compleet = "_" * len(woord)
    gegokt = False
    gegokte_letters = []
    gegokt_woorden = []
    kansen = 6
    print("hallo daar! welom bij galgje!")
    print("Bij het spel Galgje gaat het erom dat je het woord gaat raden dat is genoteerd in de woordenlijst(maar wat je niet kan zien).")
    print("Je gaat losse letters raden. Je mag maar een beperkt aantal fouten maken. Als je een fout maakt dan wordt een streepje van de galg getekend.")
    print(display_hangman(kansen))
    print(woord_compleet)
    print("\n")
    while not gegokt and kansen > 0:
        gok = input("Raad een letter: ").upper()
        if len(gok) == 1 and gok.isalpha():
            if gok in gegokte_letters:
                print("dit heb je al geprobeerd", gok, "!")
            elif gok not in woord:
                print(gok, "is niet in het woord :(")
                kansen -= 1
                gegokte_letters.append(gok)
            else:
                print("lekker bezig,", gok, "is in het woord!")
                gegokte_letters.append(gok)
                woord_as_list = list(woord_compleet)
                indices = [i for i, letter in enumerate(woord) if letter == gok]
                for index in indices:
                    woord_as_list[index] = gok
                woord_compleet = "".join(woord_as_list)
                if "_" not in woord_compleet:
                    gegokt = True
        elif len(gok) == len(woord) and gok.isalpha():
            if gok in gegokt_woorden:
                print("dit heb je al geprobeerd ", gok, "!")
            elif gok != woord:
                print(gok, " is niet in het woord :(")
                kansen -= 1
                gegokt_woorden.append(gok)
            else:
                gegokt = True
                woord_compleet = woord
        else:
            print("verkeerde input")
        print(display_hangman(kansen))
        print(woord_compleet)
        print("\n")
    if gegokt:
        print("goed gedaan, je hebt het woord geraden!")
    else:
        print("sorry, je hebt het woord niet geraden. het woord was " + woord + ". hopelijk heb je hem de volgende keer!")




def display_hangman(kansen):
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
    return stages[kansen]

def main():
    woord = get_word(woord_lijst)
    play(woord)
    while input("Nog een keer? (J/N) ").upper() == "J":
        word = get_word(woord_lijst)
        play(woord)

if __name__ == "__main__":
    main()