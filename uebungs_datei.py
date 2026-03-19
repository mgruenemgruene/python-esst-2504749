# Stein, Schere, Papier

import random

auswahl = input('Wähle Stein, Schere oder Papier: ')
print('Du hast', auswahl, 'gewählt.')

# 0=Stein / 1=Schere / 2=Papier
zufallszahl = random.randint(0, 3)
if (zufallszahl == 0):
  computer_zug = 'Stein'
elif (zufallszahl == 1):
  computer_zug = 'Schere'
else:
  computer_zug = 'Papier'
print('Ich habe zufällig', computer_zug, 'gewählt.')

# Gewinnermittlung Stein
if auswahl == 'Stein' and computer_zug == 'Stein':
  print('Unentschieden!') # Stein gg. Stein
if auswahl == 'Stein' and computer_zug == 'Schere':
  print('Du hast gewonnen!') # Stein gg Schere
if auswahl == 'Stein' and computer_zug == 'Papier':
  print('Ich habe gewonnen!') # Stein gg Papier

# Gewinnermittlung Schere
if auswahl == 'Schere' and computer_zug == 'Schere':
  print('Unentschieden!') # SSchere gg. Schere
if auswahl == 'Schere' and computer_zug == 'Stein':
  print('Ich habe gewonnen!') # Schere gg Stein
if auswahl == 'Schere' and computer_zug == 'Papier':
  print('Du hast gewonnen!') # Schere gg Papier

# Gewinnermittlung Papier
if auswahl == 'Papier' and computer_zug == 'Papier':
  print('Unentschieden!') # Papier gg. Papier
if auswahl == 'Papier' and computer_zug == 'Stein':
  print('Du hast gewonnen!') # Papier gg Stein
if auswahl == 'Papier' and computer_zug == 'Schere':
  print('Ich habe gewonnen!') # Papier gg Schere
  