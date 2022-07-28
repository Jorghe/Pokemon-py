class Ataque ():
    nombre : str
    poder_base : float
    multiplicador : float = 1.0
    def __init__ (self,nombre, poder_base, *multiplicador):
        self.nombre = nombre
        self.poder_base = poder_base
        self.multiplicador =multiplicador

chorro_de_agua = Ataque('Chorro de Agua', float(12.0), float(1.0) )
llamarada = Ataque('Llamarada', float(12.0), float(1.0))
rama_venenosa = Ataque('Rama venenosa', float(12.0), float(1.0))