class Pokemon:
    nombre : str
    def __init__(self, especie, stats, tipo, fortalezas, debilidades, ataques, defensas):
        self.especie = especie
        self.stats = stats
        self.current_stats = self.stats.copy()
        self.tipo = tipo
        self.fortalezas = fortalezas
        self.debilidades = debilidades
        self.ataques = ataques
        self.defensas = defensas

    def combate(self, combate, rival):
        print(f'El combate inicia')
    
    def nombrar_pokemon(self, nombre):
        self.nombre = nombre


squirtle = Pokemon(
    especie = "Squirtle",
    stats = {
        "velocidad": 43,
        "hp": 44,
        "ataque": 48,
        "defensa": 65},
    tipo = "agua",
    fortalezas = ["fuego"],
    debilidades = ["planta"],
    ataques = ["Chorro"],
    defensas = ["Caparazon"]
    )

charmander = Pokemon(
    especie = "Charmander",
    stats = {
        "velocidad": 65,
        "hp": 39,
        "ataque": 52,
        "defensa": 43},
    tipo = "fuego",
    fortalezas = ["planta"],
    debilidades = ["agua"],
    ataques = ["Llamarada"],
    defensas = ["Carbonifero"]
    )

bulbasaur = Pokemon(
    especie = "Bulbasaur",
    stats = {
        "velocidad": 45,
        "hp": 45,
        "ataque": 49,
        "defensa": 49},
    tipo = "planta",
    fortalezas = ["agua"],
    debilidades = ["fuego"],
    ataques = ["Veneno"],
    defensas = ["Espinas"]
    
    )