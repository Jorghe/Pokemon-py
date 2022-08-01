# Pokemon-py
Juego **Pokemon en Python** como *Challenge*

## Uso
Para correr el juego, es necesario instanciar la clase `Juego()`.

El juego te va guiando preguntando tu `nombre`, y el Pokémon a elegir.

### Ejemplo
El archivo `nuevo_juego.py` importa las librerías e instancia el objeto `Juego.Juego()` 


## Construcción
Para crear a un Pokemon, se agregaron 3 criaturas básicas de esta forma:
```
squirtle = Pokemon(
    especie = "Squirtle",
    stats = {
        "velocidad": 43,
        "ataque": 48,
        "defensa": 65},
    tipo = "agua",
    fortalezas = ["fuego"],
    debilidades = ["planta"],
    ataques = Ataque.rama_venenosa,
    defensas = ["Caparazon"]
    )
```

## Area de mejora
Debido a la poca complejidad del reto, este proyecto está por encima de los requerimientos, sin embargo, algunas mejoras a corto plazo puede ser:
- Los Ataques deberían ser una clase más compleja, integrando factores como tipo y considerar las defensas.
- Modificadores de ataques / defensas