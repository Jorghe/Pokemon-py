import Pokemon
import random

class Juego:
    nombre_jugador : str
    turno : bool
    atacante : Pokemon.Pokemon()
    defensor : Pokemon.Pokemon()

    def __init__(self):
        self.combate = ""
        self.pokemon = []
        self.turno = 0
        self.welcome()

    def welcome(self):
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

        self.atacante = yo_te_elijo

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
        
        self.defensor = rival
        
    def iniciar_juego (self, nombre, atacante, defensor):
        self.nombre_jugador = nombre
        self.atacante = atacante
        self.defensor = defensor

    def iniciar_combate(self):
        print("Inicia el combate Pokemon")
        print(f'El Pokemon {self.atacante} ha iniciado combate con {self.defensor}')

        if self.determinar_turnos():
            print('Inicias Combate')
            print(f'Pokemon {self.atacante.nombre} usa {self.atacante.ataques[0]}')
            
        else:
            print('Inicia tu rival')

        self.turno = self.determinar_turnos()

    def determinar_turnos(self)  -> bool :
        velocidad = self.atacante.stats['velocidad']
        vel_rival = self.defensor.stats['velocidad']

        if(velocidad > vel_rival):
            print(f'El jugador {self.nombre_jugador} inicia combate')
            return False
        else:
            print(f'El rival inicia combate')

            return True
