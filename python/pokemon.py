def tablaTipo (tipo1, tipo2):
    if tipo1.upper() == "FUEGO" and tipo2.upper() == "AGUA":
        return 0.5
    elif tipo1.upper() == "FUEGO" and tipo2.upper() == "PLANTA":
        return 2
    elif tipo1.upper() == "FUEGO" and tipo2.upper() == "FUEGO":
        return 0.5
    elif tipo1.upper() == "AGUA" and tipo2.upper() == "FUEGO":
        return 2
    elif tipo1.upper() == "AGUA" and tipo2.upper() == "PLANTA":
        return 0.5
    elif tipo1.upper() == "AGUA" and tipo2.upper() == "AGUA":
        return 0.5
    elif tipo1.upper() == "PLANTA" and tipo2.upper() == "FUEGO":
        return 0.5
    elif tipo1.upper() == "PLANTA" and tipo2.upper() == "AGUA":
        return 2
    elif tipo1.upper() == "PLANTA" and tipo2.upper() == "PLANTA":
        return 0.5
    elif tipo1.upper() == "NORMAL" and tipo2.upper() == "FUEGO":
        return 1
    elif tipo1.upper() == "NORMAL" and tipo2.upper() == "PLANTA":
        return 1
    elif tipo1.upper() == "NORMAL" and tipo2.upper() == "AGUA":
        return 1
    else:
        return 0

class Pokemon:
    def __init__(self, nombre, ataque, defensa, salud, tipo, movimiento1, movimiento2):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        self.tipo = tipo
        self.movimiento1 = movimiento1
        self.movimiento2 = movimiento2

    def RecibirAtaque(self, movimiento):
        potenciaRecibida = movimiento.potencia
        golpe = (potenciaRecibida / self.defensa) * tablaTipo(movimiento.tipo, self.tipo)
        self.salud = self.salud - golpe
        return "El ataque " + movimiento.nombre + " ha quitado " + str(int(golpe)) + " de salud a " + self.nombre + ", ahora tiene " + str(int(self.salud)) + " de vida !!!!!!!"

class Movimiento:
    def __init__(self, nombre, potencia, tipo):
        self.nombre = nombre
        self.potencia = potencia
        self.tipo = tipo


def atacar (pokemon):
    a = input("1:" + pokemon.movimiento1.nombre + "\n2:" + pokemon.movimiento2.nombre + "\n>")

    if int(a) == "1":
        a = pokemon.movimiento1
    elif int(a) == 2:
        a = pokemon.movimiento2
    else:
        a = pokemon.movimiento1
    return a

def info(pokemon):
    print("*** " + pokemon.nombre + "***\n\n")
    print("Salud -->\t" + str(int(pokemon.salud)))
    print("Ataque -->\t" + str(int(pokemon.ataque)))
    print("Defensa -->\t" + str(int(pokemon.defensa)))
    print("Tipo -->\t" + str(pokemon.tipo))


bulbasaur   = Pokemon("Bulbasaur", 10, 12, 23, "Planta", Movimiento("Látigo cepa", 35, "Planta"), Movimiento("Placaje", 20, "Normal"))
charmander  = Pokemon("Charmander", 15, 9, 10, "Fuego", Movimiento("Ascuas", 30, "Fuego"), Movimiento("Arañazo", 30, "Normal"))
squirtle    = Pokemon("Squirtle", 14, 13, 10, "Agua", Movimiento("Pistola agua", 35, "Agua"), Movimiento("Placaje", 20, "Normal"))

rojo=input("Dime el nombre del primer jugador: ")
pokerojo=input("Elije pokémon, " + rojo + ":")
if pokerojo.upper() == "SQUIRTLE":
    pokerojo=squirtle
elif pokerojo.upper() == "BULBASAUR":
    pokerojo=bulbasaur
else:
    pokerojo=charmander
print(rojo + " ha obtenido a " + pokerojo.nombre)

azul=input("Dime el nombre del segundo jugador: ")
pokeazul=input("Elije pokémon, " + azul + ":")
if pokeazul.upper() == "CHARMANDER":
    pokeazul=charmander
elif pokeazul.upper() == "BULBASAUR":
    pokeazul=bulbasaur
else:
    pokeazul=squirtle
print(azul + " ha obtenido a " + pokeazul.nombre)

vencedor = False
turno = True
while not vencedor:
    if turno:
        comando = input(rojo + "=>")
        if comando.upper() == "ATACAR":
            m = atacar(pokerojo)
            print(pokeazul.RecibirAtaque(m))
            turno = False
        elif comando.upper() == "INFO":
            info(pokerojo)
        elif comando.upper() == "RIVAL":
            info(pokeazul)
    else:
        comando = input(azul + "=>")
        if comando.upper() == "ATACAR":
            m = atacar(pokeazul)
            print(pokerojo.RecibirAtaque(m))
            turno = True
        elif comando.upper() == "INFO":
            info(pokeazul)
        elif comando.upper() == "RIVAL":
            info(pokerojo)