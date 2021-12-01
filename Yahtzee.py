import random

position1 = []
position2 = []
position3 = []
position4 = []
position5 = []
position6 = []
positionA = []
positionB = []
positionC = []
positionD = []
positionE = []
positionF = []
positionG = []
counter = {}
allRollsc = {}

i = 0
eindscore = 0
yahtzeecounter = 0
extrayahtzeepoints = 0
ending = ('')
extracounter = ''
rerollQuestion = False

dice = [1,2,3,4,5,6]
roll1 = random.choice(dice)
roll2 = random.choice(dice)
roll3 = random.choice(dice)
roll4 = random.choice(dice)
roll5 = random.choice(dice)

print('\nWelkom bij Yahtzee python edition!\n')

def dictonary():
    global i, allRolls
    for x in range(0,5):
        if allRolls[i] in allRollsc:
            allRollsc[allRolls[i]] += 1
            i = int(i) + 1
        else:
            allRollsc.update({allRolls[i] : 1})
            i = int(i) + 1 
        if x == 5:
            return allRollsc

def diceRoll():
    global rerollQuestion, ending 
    print('De gerolde getallen zijn:'+ str(roll1) +', ' + str(roll2) +', ' + str(roll3) + ', ' + str(roll4) + ', ' + str(roll5))
    rerollQuestion = input('Geef aan van welke positie(s) je nog een keer wilt rollen (bijv: "3 4 6 2") of typ "niks" als je niet nog een keer wilt. ')
    if rerollQuestion.lower() == 'niks':
        ending = True
        return False
    else:
        dicereroll()

def dicereroll():
    global rerollQuestion, roll1, roll2, roll3, roll4, roll5
    if '1' in rerollQuestion:
        rerollQuestion = list(rerollQuestion)
        roll1 = random.choice(dice)
    if '2' in rerollQuestion:
        rerollQuestion = list(rerollQuestion)
        roll2 = random.choice(dice)
    if '3' in rerollQuestion:
        rerollQuestion = list(rerollQuestion)
        roll3 = random.choice(dice)
    if '4' in rerollQuestion:
        rerollQuestion = list(rerollQuestion)
        roll4 = random.choice(dice)
    if '5' in rerollQuestion:
        rerollQuestion = list(rerollQuestion)
        roll5 = random.choice(dice)
    if '6' in rerollQuestion:
        rerollQuestion = list(rerollQuestion)
        roll6 = random.choice(dice)

while True:
    i = 0
    counter = {}
    rerollQuestion = ('')
    ending = False
    roll1 = random.choice(dice)
    roll2 = random.choice(dice)
    roll3 = random.choice(dice)
    roll4 = random.choice(dice)
    roll5 = random.choice(dice)
    a3ofakind = False
    a4ofakind = False
    change = False
    fullhouse = False
    largestraight = False
    smallstraight = False
    yathzee = False
    
    for x in range(0,2):
        canContinue = diceRoll()
        if canContinue == False:
            break
        else:
            continue
    
    if ending == True:
        print('De ronde in beindigd, de overgebleven cijfers zijn: '+ str(roll1) +','+ str(roll2) +','+ str(roll3) +',' + str(roll4) +','+ str(roll5))
    else:
        print('Dat was de laatse ronde, de overgebleven cijfers zijn: '+ str(roll1) +','+ str(roll2) +','+ str(roll3) +',' + str(roll4) +','+ str(roll5))
    allRolls = [roll1, roll2, roll3, roll4, roll5]
    print('Waar wil je alle cijfer zetten in deze ronde? ')
    if 1 in allRolls and not position1:
        print('Zet ' + str(allRolls.count(1) * 1) +' in het eerste vakje')
    elif not position1:
        print('Zet 0 in het eerste vakje ')
    if 2 in allRolls and not position1:
        print('Zet ' + str(allRolls.count(2) * 2) +' in het eerste vakje')
    elif not position1:
        print('Zet 0 in het tweede vakje ')
    if 3 in allRolls and not position1:
        print('Zet ' + str(allRolls.count(3) * 3) +' in het eerste vakje')
    elif not position1:
        print('Zet 0 in het derde vakje ')
    if 4 in allRolls and not position1:
        print('Zet ' + str(allRolls.count(4) * 4) +' in het eerste vakje')
    elif not position1:
        print('Zet 0 in het vierde vakje ')
    if 5 in allRolls and not position1:
        print('Zet ' + str(allRolls.count(5) * 5) +' in het eerste vakje')
    elif not position1:
        print('Zet 0 in het vijfde vakje ')
    if 6 in allRolls and not position1:
        print('Zet ' + str(allRolls.count(6) * 6) +' in het eerste vakje')
    elif not position1:
        print(' Zet 0 in het zesde vakje ')
    if allRollsc != '':
        dictonary()
    combi = roll1 + roll2 + roll3 + roll4 + roll5 
    if 3 in allRollsc.values() and not positionA or 4 in allRollsc.values() and not positionA or 5 in allRollsc.values() and not positionA :
        print("Zet "+ str(combi) + " in het three of a kind vakje")
        a3ofakind = True
    if 4 in allRollsc.values() and not positionB or 5 in allRollsc.values() and not positionB:
        print("Zet "+ str(combi) + " in het four of a kind vakje")
        a4ofakind = True
    if 3 in allRollsc.values() and 2 in allRollsc.values() and not positionC:
        print ("Zet 25 in het full house vakje")
        fullhouse = True
    if 1 in allRolls and 2 in allRolls and 3 in allRolls and 4 in allRolls and not positionD or 2 in allRolls and 3 in allRolls and 4 in allRolls and 5 in allRolls and not positionD or 3 in allRolls and 4 in allRolls and 5 in allRolls and 6 in allRolls and not positionD:
        print ("Zet 30 in het small straight vakje")
        smallstraight = True
    if 1 in allRolls and 2 in allRolls and 3 in allRolls and 4 in allRolls and 5 in allRolls and not positionE or 2 in allRolls and 3 in allRolls and 4 in allRolls and 5 in allRolls and 6 in allRolls and not positionE:
        print("Zet 40 in het large straight vakje")
        largestraight = True
    if 5 in allRollsc.values() and not positionF:
        print("Zet 50 in het yahtzee vakje")
        yahtzee = True
    if 5 in allRollsc.values() and positionF:
        print("Krijg een extra yahtzee!")
        yahtzee = True
    if not positionG:
        print("Zet "+ str(combi)+ " in het chance vakje")
        chance = True
    while True:
        choice = input("Voer de naam in van het vakje waar je een cijfer wilt ")
        if choice.lower() == "eerste" and not position1:
            position1.append(allRolls.count(1)* 1) 
            break
        elif choice.lower() == "tweede" and not position2:
            position2.append(allRolls.count(2)* 2)
            break
        elif choice.lower() == "derde" and not position3:
            position3.append(allRolls.count(3)* 3)
            break
        elif choice.lower() == "vierde" and not position4:
            position4.append(allRolls.count(4)* 4)
            break
        elif choice.lower() == "vijfde" and not position5:
            position5.append(allRolls.count(5)* 5)
            break
        elif choice.lower() == "zesde" and not position6:
            position6.append(allRolls.count(6)* 6)
            break
        elif choice.lower() == "three of a kind" and not positionA and a3ofakind == True:
            positionA.append(combi)
            break
        elif choice.lower() == "four of a kind" and not positionB and a4ofakind == True:
            positionB.append(combi)
            break
        elif choice.lower() == "full house" and not positionC and fullhouse == True:
            positionC.append(25)
            break
        elif choice.lower() == "small straight" and not positionD and smallstraight == True:
            positionD.append(30)
            break
        elif choice.lower() == "large straight" and not positionE and largestraight == True:
            positionE.append(40)
            break
        elif choice.lower() == "yahtzee" and yahtzee == True:
            if not positionF:
                positionF.append(50)
                yahtzeecounter = int(yahtzeecounter) + 1
                break
            else:
                extracounter = str(extracounter) + "X "
                extrayahtzeepoints = int(extrayahtzeepoints) + 100
                print('Je hebt meer dan 1 yahtzee! Je extra punten voor deze extra yahtzee worden op het eind bij je score geteld')
                break
        elif choice.lower() == "chance" and not positionG and chance == True:
            positionG.append(combi)
            break
        else:
            print("Oeps dat is geen mogelijke keuze mischien heb je het vakje al gevult probeer het nog eens")
            continue

    print("Een: "+str(position1))
    print("Twee: "+str(position2))
    print("Drie: "+str(position3))
    print("Vier: "+str(position4))
    print("Vijf: "+str(position5))
    print("Zes: "+str(position6))
    print("Three of a kind: "+str(positionA))
    print("Four of a kind: "+str(positionB))
    print("Full house: "+str(positionC))
    print("Small straight: "+str(positionD))
    print("Large straight: "+str(positionE))
    print("Yahtzee: "+str(positionF))
    print("Chance: "+str(positionG))    
    if not extracounter:
        pass
    else:
        print("aantal extra yahtzee's: "+ str(extracounter))

    if position1 and position2 and position3 and position4 and position5 and position6:
        if not positionA:
            positionA.append(0)
        if not positionB:
            positionB.append(0)
        if not positionC:
            positionC.append(0)
        if not positionD:
            positionD.append(0)
        if not positionE:
            positionE.append(0)
        if not positionF:
            positionF.append(0)
        if not positionG:
            positionG.append(0)

        combined = int(position1[0]) + int(position2[0]) + int(position3[0]) + int(position4[0]) + int(position5[0]) + int(position6[0])
        if combined > 63:
            eindscore = int(eindscore) + 35
        eindscore = int(combined) + int(positionA[0]) + int(positionB[0]) + int(positionC[0]) + int(positionD[0]) + int(positionE[0]) + int(positionF[0]) + int(positionG[0]) + int(extrayahtzeepoints)
        print("Dat was het spel en dit is je eindscore: ")
        print(str(eindscore))
        quit()