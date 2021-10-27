while True:
    from datetime import datetime
    import os
    now = datetime.now()
    antwoord = "Y", "y", "N","n" 
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Hello you!, ik ben Edge\n")
    c = input("Wie ben jij?\n")
    print(f"Hello {c}" " de datum en tijd is\n", now)
    antwoord = input("wil je dit progamma nog een keer doen? typ Y of N" == "Y\n")
    if (input("wil je restarten?")== "Y","y"):
     print("vaarwel")
     os.system("cls")
     continue
    else:
     print("vaarwel")
     break
     input()