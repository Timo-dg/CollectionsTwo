import random

names = []
lootjes = [] 
counter = 0
x = len(names)

print('\nSinterklaaslootjes generator\n')
print('Typ "stop" als je alle namen hebt ingevoerd.')

while True:
    names.append(input('\nInvoer van alle namen: \n'))
    if 'stop' in names:
        break
    else:
        counter += 1

names.remove('stop')
names = list(set(names))
print('\naantal namen: ' + str(counter))


for x in range(counter):
    print(random.choice(names)+ ' heeft ' + random.choice(names)) 
    