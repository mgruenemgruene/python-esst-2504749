# Das ist ein Kommentar in Ihrer Uebungsdatei

print('Hallo Welt!')

import random

auswahl = input('Wähle Stein, Schere oder Papier: ')
print('Du hast', auswahl, 'gewählt!')

# 0=Stein / 1=Schere / 2=Papier
zufallszahl = random.randint(0, 2)
if (zufallszahl == 0):
  print('Ich habe zufällig Stein gewählt!')
elif (zufallszahl == 1):
  print('Ich habe zufällig Schere gewählt!')
else:
  print('Ich habe zufällig Papier gewählt!')

# Gewinnermittlung
if (auswahl == Stein) and (zufallszahl == 0):
  print('Unentschieden!') # Stein gegen Stein
  
