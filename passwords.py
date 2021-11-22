import random
import time
import string
kleineLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
hoofdLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
specialeTekens = ['@', '#', '$', '%', '&', '_', '?', '.']
cijfers = ['0', '2', '3', '4', '5', '6', '7', '8', '9']
wachtwoord = []

for x in range (random.randint(2,6)):
    randomHoofdletters = random.randint(0,23)
    random.choice(hoofdLetters)
    wachtwoord.append(hoofdLetters[randomHoofdletters])
for x in range (random.randint(4,7)):
    randomcijfers = random.randint(0,8)
    random.choice(cijfers)
    wachtwoord.append(cijfers[randomcijfers])
for x in range(random.randint(3,3)):
    randomSpecials = random.randint(0,6)
    random.choice(specialeTekens)
    wachtwoord.append(specialeTekens[randomSpecials])
while len(wachtwoord) != 24:
    kleineLettersList = list(string.ascii_lowercase)
    randomKleineLetters = random.randint(0,23)
    wachtwoord.append(kleineLetters[randomKleineLetters])
    random.shuffle(specialeTekens)
print('Generating password...')
time.sleep(1)
print(wachtwoord)