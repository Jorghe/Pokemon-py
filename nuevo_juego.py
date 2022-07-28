import Pokemon
import Juego
import random

print(f'Bienvenido al juego Pokemon')
nombre = input('Cuál es tu nombre?')

pokemon = int(input('Elije tu pokemon [0] Squirtle, [1] Charmander, [2] Bulbasaur'))

if pokemon == 0:
    yo_te_elijo = Pokemon.squirtle
elif pokemon == 1:
    yo_te_elijo = Pokemon.charmander
elif pokemon == 2:
    yo_te_elijo = Pokemon.bulbasaur
else:
    print('Out of context')

rivales = (0,1,2)
rand_rival = random.choice(rivales)
if rand_rival == 0:
    rival = Pokemon.squirtle
elif rand_rival == 1:
    rival = Pokemon.charmander
elif rand_rival == 2:
    rival = Pokemon.bulbasaur
else:
    print('Out of context')

Juego.Juego(nombre, )