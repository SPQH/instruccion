class Persona:
    def __init__(self, n, p):
        self.peso = p
        self.nombre = n

    def masPesado(self):
        self.peso = self.peso * 1000

    def aumentoPeso(self, a):
        self.peso = self.peso + a


def comprobacion (a, b):
    if a == b:
        return "e"
    elif (a == "Piedra" and b == "Tijera") or (a == "Tijera" and b == "Papel") or (a == "Papel" and b == "Piedra") :
        return "a"
    else:
        return "b"


alberto = Persona("Juan", 100110)
alberto.nombre = "Alberto"
alberto.masPesado()

javier = Persona("Javier", 8000)
javier.aumentoPeso(-1000)
print("La persona que se llama " +  alberto.nombre + " pesa " + str(alberto.peso) + " y " + javier.nombre + " pesa " + str(javier.peso))

jugando = True
while jugando:
    jugador1 = input("Piedra/Papel/Tijera")
    jugador2 = input("Piedra/Papel/Tijera")

    r = comprobacion(jugador1, jugador2)
    if r == "e":
        print("Empate!")
    elif r == "a":
        print("Gana jugador 1!")
    else:
        print("Gana jugador 2!")



