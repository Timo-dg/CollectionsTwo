mylist = []
myTup = ()

print('\nBoodschappenlijstje\n')
def programma():
    itemName = input('Welk item wilt u toevoegen aan het boodschappenlijstje? ')
    itemAmount = input('Hoeveel items wilt u hiervan? ')
    toevoegen = input('Wilt u nog meer boodschappen toevoegen? ja/nee ').lower()
    if toevoegen == 'ja':
        myTup = (itemAmount, itemName)
        mylist.append(myTup)
        [mylist.append(x) for x in mylist if x not in mylist]
        programma()
    else:
        myTup = (itemAmount, itemName)
        mylist.append(myTup)
        mylist.sort()
        print(mylist)

programma()