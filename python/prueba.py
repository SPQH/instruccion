
print("RESULTADOS TEST CORONAVIRUS")
print("Por favor, confirme sus datos personales para acceder a los resultados del test: ")

nombre= "Alberto Balon Salado"
direccion= "Calle Reyes Catolicos"
ntest= 342221
nombre=input("Nombre completo: ")
direccion=input("Domicilio: ")
ntest=int(input("Identificador de la prueba: "))

if nombre != "Alberto Balon Salado" and direccion != "Calle Reyes Catolicos" and ntest != 342221:
    print("Sus datos no se corresponden con los asociados a este documento. Por favor, intentelo de nuevo.")
elif nombre == "Alberto Balon Salado" or direccion == "Calle Reyes Catolicos" or ntest == 342221:
    print("Hola Sensi")
else:
    print("Hola Alberto, has accedido correctamente. Su prueba ha resultado positiva por COVID.")

    print("Hola")

