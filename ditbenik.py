while True:
    from datetime import datetime
    import os
    now = datetime.now()
    antwoord ="A","B","C"
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    print("Hello you!, ik ben Edge\n")
    c = input("Wie ben jij?\n")
    print()
    print(f"Hello {c}. ik ben een nieuwkomer op het Mediacollege Amsterdam.")
    print("door deze vraag te beantwoorden kan je mij beter leren kennen.")
    print()
    print("A. Ik heb twee honden en een cavia.")
    print("B. Ik heb op het Haarlem college gezeten.")
    print("C. Ik heb 7 jaar op basketbal gezeten.")
    print()
    antwoord = input("antwoord A, B of C wat je denkt dat waar is>>>>")
    if antwoord.upper() == "C":
     print("Juist. Ik heb inderdaad 7 jaar op basketbal gezeten.",now)
    elif antwoord.upper() == "B":
     print("Onjuist. Ik heb op het paulusmavo gezeten.",now)
    elif antwoord.upper() == "A":
     print("Onjuist. Ik heb twee katten en een cavia gehad.", now)
    print()
    print("A. Mijn favoriete game is Warframe.")
    print("B. Ik woon samen met mijn zus in Amsterdam.")
    print("C. Ik ben een groot fan van voetbal.")
    print()
    antwoord = input("antwoord A, B of C wat je denkt dat waar is>>>>")
    if antwoord.upper() == "A":
     print("Juist. Ik heb in Warframe de meeste uren zitten en speel het wanneer ik niet weet wat ik moet doen.",now)
    elif antwoord.upper() == "B":
     print("Onjuist. Ik woon nog samen bij mijn ouders terwijl mijn zus in amsterdam woont.",now)
    elif antwoord.upper() == "C":
     print("Onjuist. Ik ben niet echt geinteresseerd in voetbal.", now)
    print()
    print("A. Ik ben momenteel 17 jaar oud.")
    print("B. Ik heb mijn middelbare school afgerond met havo.")
    print("C. Mijn rode haar komt van mijn moeders kant.")
    print()
    antwoord = input("antwoord A, B of C wat je denkt dat waar is>>>>")
    if antwoord.upper() == "A":
     print("juist. Ik ben geboren op 6 november 2003.",now)
    elif antwoord.upper() == "B":
     print("onjuist. Ik heb mijn middelbare school afgerond met een vmbo kader diploma.",now)
    elif antwoord.upper() == "C":
     print("onjuist. Ik heb het van mijn vader net zoals mijn naam.", now)
    break
    input()

    