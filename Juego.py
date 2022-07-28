import Pokemon
import random

class Juego:
    nombre_jugador : str
    turno : bool
    atacante : Pokemon.Pokemon
    defensor : Pokemon.Pokemon
    ronda : int = 0
    atacante_inicia : bool
    batalla_activa : bool = False

    def __init__(self):
        self.combate = ""
        self.pokemon = []
        self.welcome()

    def welcome(self):
        print(f'Bienvenido al juego Pokemon')
        nombre = input('Cuál es tu nombre? \n')
        pokemon = int(input('Elije tu pokemon [0] Squirtle, [1] Charmander, [2] Bulbasaur \n' ))

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

        self.iniciar_juego(nombre, self.atacante, self.defensor)
        
    def iniciar_juego (self, nombre, atacante, defensor):
        self.nombre_jugador = nombre
        self.atacante = atacante
        self.defensor = defensor

        print(f"{nombre}, has elegido a {atacante.especie} ")
        print(f"El destino ha elegido a {defensor.especie} como rival")

        self.iniciar_combate()

    def iniciar_combate(self):
        print("Inicia el combate Pokemon")
        self.batalla_activa = True
        # print(f'El Pokemon {self.atacante} ha iniciado combate con {self.defensor}')

        if self.determinar_turnos():
            print('Inicias Combate')
            print(f'Pokemon {self.atacante.especie} usa {self.atacante.ataques.title()}')
            self.atacante_inicia = True
            
        else:
            print('Inicia tu rival')
            self.atacante_inicia = False
        
        self.comenzar_rondas()

    def comenzar_rondas (self):
        multiplicador_suerte = 1.0
        multiplicador_rival = 0.9
        while(self.batalla_activa):

            if(self.atacante_inicia):
                print(f"{self.defensor.especie} ha recibido {self.atacante.ataques.dano}")
                self.defensor.hp -= self.atacante.ataques.dano * multiplicador_suerte
            else:
                print(f"{self.atacante.especie} ha recibido {self.defensor.ataques.dano} ")
                self.atacante.hp -= self.defensor.ataques.dano * multiplicador_rival

            self.atacante_inicia = not self.atacante_inicia

            if(self.atacante.hp <= 0 or self.defensor.hp <= 0):
                campeon = "" # cmp = lambda x, y : x > y

                if(self.atacante.hp > self.defensor.hp):
                    campeon = self.atacante.especie
                else:
                    campeon = self.defensor.especie
                print(f"La batalla ha terminado, el campeón es : {campeon} ") 
                self.batalla_activa = False

    def determinar_turnos(self)  -> bool :
        velocidad = self.atacante.stats['velocidad']
        vel_rival = self.defensor.stats['velocidad']

        if(velocidad > vel_rival):
            print(f'El jugador {self.nombre_jugador} inicia combate')
            return False
        else:
            print(f'El rival inicia combate')
            return True
