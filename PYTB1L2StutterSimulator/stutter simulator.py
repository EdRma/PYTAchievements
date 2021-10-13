print("di... di...dit is de st... st... stotter si... si... simulator")
print("ty... ty... type hi... hi... hier wat je wi... wi... wilt la... la... laten st... st... stotteren")
running = True
while running == True:
    antwoord = input("vu...vul in...: ")
    print("")
    userlist = antwoord.split()
    for x in userlist:
        if len(x) > 2:
            print(x[0:2]+"...", x[0:2]+"..." ,x)
        else:
            print(x)
            