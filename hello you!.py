from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("datum en tijd =\n", dt_string)
print("Hello you!, ik ben Edge\n")
c = input("Wie ben jij?\n")
print(f"Hello {c}\n")
print("de datum en tijd is\n", now)
if (input("wil je dit progamma nog een keer doen? typ Y of N")== "Y\n"):
 input()