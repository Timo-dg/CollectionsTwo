import random
counter = 0
global compleetdeck
compleetdeck = []
playerhand = []
aihand = []
stapel = []
nuSpeelbaar = []
kanGeelSpelen = False
KanRoodSpelen = False
kanGroenSpelen = False
kanBlauwSpelen = False
kleuren = ["blauw","rood","groen","geel"]
nummersetc = ["0","1","2","3","4","5","6","7","8","9","+2","omkeer","sla-beurt-over"]
eindeSpel = False
heeftNummersOfSpecails = False
viercounter = 0
keuzecounter = 0
volgendeSpelerSkip = 0
hebJeGelijkSpel = False
kleurendictionary = {
    "rood" : 0,
    "blauw" : 0,
    "groen" : 0,
    "geel" : 0
}

def showDevinfo ():
        print("de lijst van speelbare kaarten: "+ ", ".join(nuSpeelbaar))
        print("de stapel in het midden van de tafel: "+ ", ".join(stapel))
        print("je huidige hand: "+ ", ".join(playerhand))
        print("de huidige hand van de vijand: " + ", ".join(aihand))

def generateCards(deck, cardtypes):
    for currentcard in deck:
        for currenttype in cardtypes:
            compleetdeck.append(currentcard + " " + currenttype)
    random.shuffle(compleetdeck)
    return [compleetdeck]

def playerDraws():
    global nextcard, hebJeGelijkSpel
    if not nuSpeelbaar:
        hebJeGelijkSpel = True
        nextcard = compleetdeck[0]
        del compleetdeck[0]
        print("Je hebt geen kaarten om te spelen dus je pakt eentje van de stapel")
        for x in kleuren:
            if x in nextcard and x not in stapel[-1]:
                print("De kaart die je hebt gepakt van de stapel is "+ str(nextcard) +", die kan je niet spelen")
                playerhand.append(nextcard)
                nextcard = ""
        for x in kleuren:
            if x in nextcard and x in stapel[-1]:
                while True:
                    immediatelyplay = input("De kaart die je hebt gepakt van de stapel is "+ str(nextcard) +", je kan die kaart meteen spelen, wil je dat doen? ")
                    if immediatelyplay.lower() == "ja":
                        stapel.append(nextcard)
                        nextcard = ""
                        print("De kaart die boven aan de stapel ligt is "+ stapel[-1])
                        break
                    elif immediatelyplay.lower() == "nee":
                        playerhand.append(nextcard)
                        nextcard = ""
                        print("De kaart die boven aan de stapel ligt is "+ stapel[-1])
                        break
                    elif immediatelyplay.lower() == "quit":
                        quit()
                    elif immediatelyplay.lower() == "show":
                        showDevinfo()
                        continue
                    else:
                        print("oeps, dat snapte ik niet. de correcte inputs zijn ja en nee")
                        continue

def aiDraws():
    pass

def aiTurn():
    global nextcard, eindeSpel, aihand, aiSkips, volgendeSpelerSkip
    print("De hand van je vijand bestaat uit "+ str(len(aihand)) +" kaarten")
    if len(aihand) == 0:
        eindeSpel = True
    if len(stapel) != 1:
        if "+2" in stapel[-1]:
            print("Je vijand moet 2 kaarten pakken door jou +2 kaart")
            for x in range(0,2):
                nextcard = compleetdeck[0]
                del compleetdeck[0]
                aihand.append(nextcard)
        elif volgendeSpelerSkip > 0:
            print("je vijand moest zijn beurt overslaan door jou sla-beurt-over/omkeer kaart")
            volgendeSpelerSkip = int(volgendeSpelerSkip) - 1
        elif "neem vier" in stapel[-1]:
            print("Je vijand moet 4 kaarten pakken door jou neem vier kaart")
            for x in range(0,4):
                nextcard = compleetdeck[0]
                del compleetdeck[0]
                aihand.append(nextcard)
    for x in aihand:
        if "geel" in x:
            kleurendictionary["geel"] += 1
        elif "rood" in x:
            kleurendictionary["rood"] += 1
        elif "groen" in x:
            kleurendictionary["groen"] += 1
        elif "blauw" in x:
            kleurendictionary["blauw"] += 1
      
    max_key = max(kleurendictionary, key=kleurendictionary.get)
    


    if volgendeSpelerSkip == 0:
        aiChecksForAllColors()
        aicChecksForAllNumbersAndSpecialCards()
        if kanBlauwSpelen == True or kanGroenSpelen == True or kanGeelSpelen == True or KanRoodSpelen == True or heeftNummersOfSpecails == True or "Keuzekaart" in stapel[-1] or "neem vier" in stapel[-1] or "neem vier" in playerhand or "Keuzekaart" in playerhand and not nuSpeelbaar:        
            pass
    elif volgendeSpelerSkip == 1:
        print("je vijand moest zijn beurt overslaan door jou sla-beurt-over/omkeer kaart")
        volgendeSpelerSkip = int(volgendeSpelerSkip) - 1

def playerTurn():
    global nextcard, eindeSpel, volgendeSpelerSkip
    if not stapel:
        nextcard = compleetdeck[0]
        del compleetdeck[0]
        stapel.append(nextcard)
    if len(playerhand) == 0:
        eindeSpel = True
    
    if volgendeSpelerSkip == 0 and eindeSpel == False and len(stapel) != 1:
        if "+2" in stapel[-1]:
            print("je moest 2 kaarten pakken door de +2 kaart die je vijand heeft gespeeld")
            for x in range(0,2):
                nextcard = compleetdeck[0]
                del compleetdeck[0]
                playerhand.append(nextcard)
        elif "neem vier" in stapel[-1]:
            print("je moet 4 kaarten pakken door de vijand's neem vier kaart")
            for x in range (0,4):
                nextcard = compleetdeck[0]
                del compleetdeck[0]
                playerhand.append(nextcard)

    if volgendeSpelerSkip == 0 and eindeSpel == False:
        print("Het is jouw beurt, je kaarten zijn: "+ ", ".join(playerhand))

        print("De kaart die boven aan de stapel ligt is "+ stapel[-1])
        checkForAllColors()
        if hebJeGelijkSpel == False:
            checkForAllNumbersAndSpecialCards()
            if kanBlauwSpelen == True or kanGroenSpelen == True or kanGeelSpelen == True or KanRoodSpelen == True or heeftNummersOfSpecails == True or "Keuzekaart" in stapel[-1] or "neem vier" in stapel[-1] or "neem vier" in playerhand or "Keuzekaart" in playerhand and nuSpeelbaar and hebJeGelijkSpel == False:
                print("Je hebt kaarten die je kan spelen!")

                print("De speelbare kaarten zijn "+ ", ".join(nuSpeelbaar) +". Geef de positie aan van de kaart die je wilt spelen (geteld van links)")
                while True:
                    whattoplay = input("")
                    if whattoplay.isnumeric() == True and int(whattoplay) > 0 and int(whattoplay) <= len(nuSpeelbaar):
                        stapel.append(nuSpeelbaar[int(whattoplay) - 1])
                        for x in playerhand:
                            if nuSpeelbaar[int(whattoplay) - 1] ==  x:
                                playerhand.remove(x)
                                break
                        print("De kaart die boven aan de stapel ligt is "+ stapel[-1])
                        if "Keuzekaart" in stapel[-1]:
                            print("Je hebt zojuist een keuzekaart gespeeld, welke kleur wil je hebben?")
                            while True:
                                chooseColor = input("")
                                if "geel" in chooseColor or "groen" in chooseColor or "rood" in chooseColor or "blauw" in chooseColor:
                                    del stapel[-1]
                                    stapel.append("Keuzekaart "+ str(chooseColor))
                                    print("De kaart die boven aan de stapel ligt is "+ stapel[-1])
                                    break
                        if "neem vier" in stapel[-1]:
                            print("Je hebt zojuist een neem vier kaart gespeeld, je vijand moet 4 kaarten pakken maar jij mag ook de kleur kiezen, welke kleur wil je hebben?")
                            while True:
                                chooseColor = input("")
                                if "geel" in chooseColor or "groen" in chooseColor or "rood" in chooseColor or "blauw" in chooseColor:
                                    del stapel[-1]
                                    stapel.append("neem vier "+ str(chooseColor))
                                    print("De kaart die boven aan de stapel ligt is "+ stapel[-1])
                                    break
                        break
                    elif whattoplay.lower() == "quit":
                        quit()
                    elif whattoplay.lower() == "show":
                        showDevinfo()
                        continue
                    else:
                        print("Vul een geldig nummer van de positie die u heeft")
                        continue
            print("Dat was het eidne van jouw beurt, het is nu de beurt van je vijand")
            print("")
    elif eindeSpel == False:
        print("je moet je beurt overslaan door je vijand's sla-beurt-over/omkeer kaart")
        volgendeSpelerSkip = int(volgendeSpelerSkip) - 1

def aiChecksForBlue():
    global kanBlauwSpelen
    if "blauw" in stapel[-1]:
        for x in aihand:
            if "blauw" in x:
                nuSpeelbaar.append(x)
        if nuSpeelbaar:
            kanBlauwSpelen = True

def aiChecksForRed():
    global KanRoodSpelen
    if "rood" in stapel[-1]:
        for x in aihand:
            if 'blauw' in x:
                nuSpeelbaar.append(x)
        if nuSpeelbaar:
            KanRoodSpelen = True

def aiChecksForGreen():
    global kanGroenSpelen
    if "groen" in stapel[-1]:
        for x in aihand:
            if "groen" in x:
                nuSpeelbaar.append(x)
        if nuSpeelbaar:
            kanGroenSpelen = True

def aiChecksForYellow():
    global kanGeelSpelen
    if "yellow" in stapel[-1]:
        for x in aihand:
            if "groen" in x:
                nuSpeelbaar.append(x)
        if nuSpeelbaar:
            kanGeelSpelen = True

def checkForBlue():
    global kanBlauwSpelen
    if "blauw" in stapel[-1]:
        for x in playerhand:
            if  "blauw" in x:
                nuSpeelbaar.append(x)   
        if nuSpeelbaar:
            kanBlauwSpelen = True
    
def checkForRed():
    global KanRoodSpelen
    if "rood" in stapel[-1]:
        for x in playerhand:
            if  "rood" in x:
                nuSpeelbaar.append(x)   
        if nuSpeelbaar:
            KanRoodSpelen = True

def checkForYellow():
    global kanGeelSpelen
    if "geel" in stapel[-1]:
        for x in playerhand:
            if  "geel" in x:
                nuSpeelbaar.append(x)   
        if nuSpeelbaar:
            kanGeelSpelen = True

def checkForGreen():
    global kanGroenSpelen
    if "groen" in stapel[-1]:
        for x in playerhand:
            if  "groen" in x:
                nuSpeelbaar.append(x)   
        if nuSpeelbaar:
            kanGroenSpelen = True

def aicChecksForAllNumbersAndSpecialCards():
    global aihand, heeftNummersOfSpecails, viercounter, keuzecounter
    for x in aihand:
        if "sla-beurt-over" in x and "sla-beurt-over" in stapel[-1] or "+2" in x and "+2" in stapel[-1] or "omkeer" in x and "omkeer" in stapel[-1] or "1" in x and "1" in stapel[-1] or "2" in x and "2" in stapel[-1] or "3" in x and "3" in stapel[-1] or "4" in x and "4" in stapel[-1] or "5" in x and "5" in stapel[-1] or "6" in x and "6" in stapel[-1] or "7" in x and "7" in stapel[-1] or "8" in x and "8" in stapel[-1] or "8" in x and "8" in stapel[-1] or "9" in x and "9" in stapel[-1] or "0" in x and "0" in stapel[-1]:
            nuSpeelbaar.append(x)
            heeftNummersOfSpecails = True

def checkForAllNumbersAndSpecialCards():
    global playerhand, heeftNummersOfSpecails, viercounter, keuzecounter
    for x in playerhand:
        if "sla-beurt-over" in x and "sla-beurt-over" in stapel[-1] or "+2" in x and "+2" in stapel[-1] or "omkeer" in x and "omkeer" in stapel[-1] or "1" in x and "1" in stapel[-1] or "2" in x and "2" in stapel[-1] or "3" in x and "3" in stapel[-1] or "4" in x and "4" in stapel[-1] or "5" in x and "5" in stapel[-1] or "6" in x and "6" in stapel[-1] or "7" in x and "7" in stapel[-1] or "8" in x and "8" in stapel[-1] or "8" in x and "8" in stapel[-1] or "9" in x and "9" in stapel[-1] or "0" in x and "0" in stapel[-1] or "Keuzekaart" in x or "neem vier" in x:
            nuSpeelbaar.append(x)
            heeftNummersOfSpecails = True 
    

def aiChecksForAllColors():
    aiChecksForBlue()
    aiChecksForGreen()
    aiChecksForYellow()
    aiChecksForRed()
    if kanBlauwSpelen == False and KanRoodSpelen == False and kanGroenSpelen == False and kanGeelSpelen == False and heeftNummersOfSpecails == False:
        playerDraws()
    
def checkForAllColors():
    checkForBlue()
    checkForGreen()
    checkForRed()
    checkForYellow()
    if "Keuzekaart" in stapel[-1] and len(stapel) == 1:
        print("De kaart op het begin van de stapel is een keuzekaart dus jij mag de kleur bepalen")
        while True:
            choosecolor = input("Welke kleur wil je hebben? ")
            if choosecolor.lower() in kleuren:
                stapel.append(choosecolor)
                nuSpeelbaar.append("Keuzekaart")
                break
            elif choosecolor.lower() == "quit":
                quit()
            elif choosecolor.lower() == "show":
                showDevinfo()
            else:
                print("oeps, dat snapte ik niet. de correcte inputs zijn rood, blauw, geel en groen ")
                continue
        print(stapel[-1])        
    elif "neem vier" in stapel[-1] and len(stapel) == 1:
        print("De kaart op het begin van de stapel is een neem vier dus jij mag de kleur bepalen")
        while True:
            choosecolor = input("Welke kleur wil je hebben? ")
            if choosecolor.lower() in kleuren:
                stapel.append(choosecolor)
                nuSpeelbaar.append("neem vier")
                break
            elif choosecolor.lower() == "quit":
                quit()
            elif choosecolor.lower() == "show":
                showDevinfo()
                continue
            else:
                print("oeps, dat snapte ik niet. de correcte inputs zijn rood, blauw, geel en groen ")
                continue
    elif kanBlauwSpelen == False and KanRoodSpelen == False and kanGroenSpelen == False and kanGeelSpelen == False and heeftNummersOfSpecails == False:
        playerDraws()


completedeck = generateCards({"geel", "groen", "rood","blauw"}, ["0","1","2","3","4","5","6","7","8","9","+2","omkeer","sla-beurt-over"])
completedeck += generateCards({"geel", "groen", "rood","blauw"}, ["1","2","3","4","5","6","7","8","9","+2","omkeer","sla-beurt-over"])

playerhand = (compleetdeck[0:7])
aihand = (compleetdeck[7:14])
del compleetdeck[:14]
while True:
    playerTurn()
    kanBlauwSpelen = False
    kanGroenSpelen = False
    kanGeelSpelen = False
    KanRoodSpelen = False
    nuSpeelbaar = []
    heeftNummersOfSpecails = False
    hebJeGelijkSpel = False
    aiTurn()
    hebJeGelijkSpel = False
    kanBlauwSpelen = False
    kanGroenSpelen = False
    kanGeelSpelen = False
    KanRoodSpelen = False
    nuSpeelbaar = []
    heeftNummersOfSpecails = False
    if eindeSpel == True:
        print("Dat is het einde van het spel!")
        quit()