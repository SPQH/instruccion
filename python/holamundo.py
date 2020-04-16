v=5
tupla = ("Alberto", v, 65.8, 12)
lista = [
    ["Alberto", "Javier", "Dani", "Jorge", "Manuel1", "Miguel", "Alberto", "Javier", "Dani", "Jorge", "Manuel", "Miguel", "Alberto", "Javier", "Dani", "Jorge", "Manuel", "Miguel"], # 0
    ["Alberto", "Javier", "Dani", "Jorge", "Manuel2", "Miguel", "Alberto", "Javier", "Dani", "Jorge", "Manuel", "Miguel", "Alberto", "Javier", "Dani", "Jorge", "Manuel", "Miguel"], # 1
    ["Alberto", "Javier", "Dani", "Jorge", "Manuel3", "Miguel", "Alberto", "Javier", "Dani", "Jorge", "Manuel", "Miguel", "Alberto", "Javier", "Dani", "Jorge", "Manuel", "Miguel"], # 2
    ["Alberto", "Javier", "Dani", "Jorge", "Manuel4", "Miguel", "Alberto", "Javier", "Dani", "Jorge", "Manuel", "Miguel", "Alberto", "Javier", "Dani", "Jorge", "Manuel", "Miguel"]  # 3
    ]
diccionario= {'kg': 20, 'm': 1.8, 'color': 'rojo'}
print(diccionario.get('kg'))

lista.pop(1)
lista[1].remove("Alberto")
print(lista[1][4])


nombre=input("Dime tu nombre: ")
print("Hola mundo, " + nombre.upper() + " capullo")
print("Hola mundo, " + nombre.lower() + " capullo")
print("Hola mundo, " + nombre.title() + " capullo")

edad=int(input("¿Cuantos años tienes?: "))
print("Tienes " + str(edad) + " años")

resta=100-edad # int (integer) es número entero / float (floating) es número flotante (decimal)
print("Hola " + nombre + " tienes " + str(edad) + " años y te faltan " + str(resta) + " para llegar a los 100") # str (string) es texto

if edad > 80 or nombre != "Alberto":
    print("Qué viejo")
    print("jaja")
elif edad < 0:
    print("No has nacido?")
elif nombre == "Javier":
    print("jeje")
else:
    print("Ah vaya")


while True:
    esHereje=input("¿Eres hereje? (Si/No): ").title()

    if esHereje == "Si":
        print("Conviértete")
        break
    elif esHereje == "No":
        print("Bienaventurado")
        break
    else:
        print("No me has dicho ni si ni no, imbécil")



for i in lista:
    #if i == "Miguel":
    #    print("Hola Don Miguel")
    for e in i:
        print("Iterador número " + str(e))