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


esHereje=input("¿Eres hereje? (Si/No): ").title()

if esHereje == "Si":
    print("Conviértete")
elif esHereje == "No":
    print("Bienaventurado")
else:
    print("No me has dicho ni si ni no, imbécil")
