print("doel te behalen: om 9 uur op school komen")
antwoord1 = input ("je wordt om half 8 wakker, ga je ombijten of aankleden? typ O of A: ")

if antwoord1.upper()== "O":
    print("je gaat naar beneden om een broodje te maken en op je ipad te kijken of er nog iets is gebeurd")
    antwoord2 = input("ga je nu douchen of je spullen inpakken? typ D of S: ")

    if antwoord2.upper()=="D":
        print("je stapt onder de douche en kleed je daarna aan")
        print("je loopt naar het station maar bent erachter gekomen dat je hem hebt gemist hierdoor zal je telaat komen en is nu het spel voorbij")

    elif antwoord2.upper()=="S":
        print("je pakt je spullen in en kleed je aan omdat het al bijna 8 uur is")
        print("je loopt naar de trein en stapt in onderweg naar amsterdam sloterdijk")
        print("je komt aan op amsterdam slooterdijk en loopt naar het mediacollege")
        print("je hebt het optijd gehaald en dus het spel gewonnen")



elif antwoord1.upper() == "A":
    print("je gaat douchen en je aankleden")
    print("je gaat naar beneden om een broodje te maken en op te eten")
    antwoord3 = input("ga je nu eten of je spullen inpakken? typ E of S: ")

    if antwoord3.upper()=="D":
        print("je gaat naar beneden om een broodje te maken en op te eten")
        print("je pakt je spullen in en rent naar het station om nog net de trein te halen onderweg naar amsterdam sloterdijk")
        print("je komt aan op amsterdam slooterdijk en loopt naar het mediacollege")
        print("je hebt het optijd gehaald en dus het spel gewonnen")

    elif antwoord3.upper()=="S":
        print("je pakt je spullen in ")
        print("je loopt naar de trein en stapt in onderweg naar amsterdam sloterdijk")
        print("je komt aan op amsterdam slooterdijk en loopt naar het mediacollege")
        print("je hebt het optijd gehaald en dus het pel gewonnen")