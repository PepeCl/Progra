# ------ NO BORRAR -----
from funciones import *
from herramientas import *
# ------ NO BORRAR -----

user = {}
menu = ["Revisar menú",
        "Revisar carrito",
        "Pagar",
        "Quitar ítem de carrito",
        "Modificar Item del Menú",
        "Agregar Item al Menú",
        "Salir"]

##### SE ASUME QUE LOS DATOS DEL ARCHIVO CSV ESTARÁN INGRESADOS CORRECTAMENTE, SIN ESPACIOS DENTRO DEL DATO COMO ESTABA EN EL ARCHIVO INICIAL ######

#Acciones Iniciales

nombre = input("Ingrese su nombre: ")
comida_favorita = input("Ingrese su comida favorita: ")
pregunta = input("Es alergíco a algún ingrediente? (Y/N): ")
if pregunta == "Y":
    alergias = input("Ingrese los ingredientes a los que es alérgico bajo el siguiente formato: (ingrediente 1, ingrediente 2, ingrediente 3, ....): ") #se asume que el cliente ingresa correctamente los datos bajo el formato
    lista_alergias = alergias.split(",") #se crea una lista de ingredientes a los que el usuario es alérgico
    print(lista_alergias) #se imprime la lista de alergias
else: #condicion de que la persona no tenga alergias
    print("Nos alegramos que no posea alergias")

user["nombre"] = nombre #se asigna el nombre de usuario con el nombre ingresado
print("Bienvenido Don",nombre)

#menu principal
while (True):
    for i,opciones in enumerate(menu):
        print(f"{i+1}: {opciones}") #despliega el menu completo con numeración de cada opción

    eleccion = int(input("Ingrese la acción del menú a realizar: "))
    seleccion = menu[eleccion-1]

    print(seleccion) #imprime la selección del usuario

    if eleccion == 1:
        rev_menu(var) #llama a la funcion de revisar menú

    if eleccion == 2:
        print(carrito_compras) #imprime el carrito de compras

    if eleccion == 3:
        print("El precio sin propina es: $" ,pagar(carrito_compras)) #llama a la funcion pagar()
        print("***Elija una opción***")
        tip = input("1:Pagar (Se agrega una propina de 10%)\n2:Seguir Comprando\n").upper() #pregunta al usuario si desea pagar o seguir comprando
        if tip == "1":
            total = pagar(carrito_compras) * 1.1 #se agrega la propina del 10%
            print("El total a pagar es: $",total) 
            carrito_compras =[] #se vacía la lista del usuario
        if tip == "2":
            pass #simplemente pasa si se elige seguir comprando y vuelve al menú principal
    
    if eleccion == 4:
        if carrito_compras: #si el carrito tiene elementos entonces esta condición será True y procede a su ejecución
            for i,elementos in enumerate(carrito_compras):
                print((i+1), "-->",elementos) #despliega la lista de elementos del carrito de compras con su respectivo ID
            id_carrito = int(input("Ingrese el ID para eliminar el item del carrito: "))
            carrito_compras.pop(id_carrito-1) #elimina el ID seleccionado por el usuario
            print("***Su nuevo carrito de compras***")
            print(carrito_compras) #imprime el nuevo carrito de compras
            print("******")
        else: #Condición de carrito vacío
            print("Su carrito no tiene elementos")


    if eleccion == 5:
        contra = input("Ingrese la contraseña: ")
        if check_password(contra): #si la contraseña es correcta la función retorna True y procede a la ejecución del código siguiente
            for i,elementos in enumerate(var):
                print((i+1),"-->",elementos ) #despliega la lista de elementos del carrito de compras con su respectivo ID
            id = int(input("Ingrese el ID que desea modificar: ")) #se asume que se ingresa un ID dentro de la lista
            item = input("Ingrese la característica a modificar (nombre,precio,kcal,ingredientes): ").lower() #se asume que se ingresa el dato correctamente
            mod = input("Ingrese el nuevo atributo: ")
            nuevo = var[id] #la variable "nuevo" toma el valor de un diccionario elegido dentro de la lista de diccionarios
            nuevo[item] = mod #se modifica el atributo bajo los métodos de diccionarios
        else: #condición de contraseña incorrecta 
            print("Contraseña incorrecta x_x")
        print(var)

    if eleccion == 6:
        contra = input("Ingrese la contraseña: ")
        if check_password(contra): #si la contraseña es correcta la función retorna True y procede a la ejecución del código siguiente
            nombre = input("Ingrese el nombre del nuevo plato: ") 
            precio = int(input("Ingrese el precio: "))
            kcal = float(input("Ingrese las calorias del plato: "))
            ingredientes = input("Ingrese los ingredientes bajo el siguiente formato (ingrediente 1, ingrediente 2, ...)") #se asume que el usuario ingresa correctamente los ingredientes bajo el formato
            lista_ingredientes = ingredientes.split(",") #con el comando split creo una lista de ingredientes
        var.append(agregar_items(nombre,precio,kcal,lista_ingredientes)) #llamo a la función agregar_items y creo un nuevo item
        print("El nuevo menú es: ",var) #se despliega el nuevo menú
    
    if eleccion == 7: #condición de salida
        print("Hasta pronto :D")
        break
        

   