# Das ist ein Kommentar in Ihrer Uebungsdatei

print('Hallo Welt!')

import random

auswahl = input('Wähle Stein, Schere oder Papier: ')
print('Du hast', auswahl, 'gewählt.')

# 0=Stein / 1=Schere / 2=Papier
zufallszahl = random.randint(0, 2)
if (zufallszahl == 0):
  computer_zug = 'Stein'
elif (zufallszahl == 1):
  computer_zug = 'Schere'
else:
  computer_zug = 'Papier'
print('Ich habe zufällig', computer_zug, 'gewählt.')

# Gewinnermittlung
