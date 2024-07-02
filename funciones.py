"""
Puede escribir aqui las funciones del codigo
Se importaran de forma automatica al 'main.py'
"""
# ------ NO BORRAR -----
def test () -> None:
    """
        Funcion para probar el archivo
    """
    import herramientas
    menu = herramientas.load_items('menu.csv')
    print(menu)

# esto es para que test solo corra si es ejecutado directamente
if __name__ == '__main__':
    test()
# ------ NO BORRAR -----

#Escribir Funciones desde aqui hacia abajo ------------
carrito_compras = [] #lista vacía de carrito de compras
precio_carrito = [] #lista vacía de precios
#ejemplo de funcion

def rev_menu(datos):
    for elementos in datos: #recorro la lista de diccionarios
        print(elementos["nombre"], "|","Precio =", elementos["precio"]) #imprimo cada nombre de item y su precio respectivo
    while True: #bucle para ingresar elementos al carrito
        carrito = input("Ingrese el nombre del producto para agregar a su carrito: ") #se asume que el usuario ingresará un dato válido, es decir, un ítem de la lista
        for ele in datos: #recorro la lista de diccionarios
            if ele["nombre"] == carrito: #si el nombre del producto coincide con alguno de la lista de menú
                carrito_compras.append(ele) #entonces se agrega al carrito
        opcion = input("Desea agregar otro item a su carrito? Y/N: ").upper() #condicion de seguir agregando elementos al carrito
        if opcion == "Y":
            continue
        if opcion == "N":
            break

def pagar(datos):
    precio_total = 0
    for elementos in datos: #recorro la lista de diccionarios
        precio_carrito.append(elementos["precio"]) #obtengo el precio de cada elemento de la lista y lo agrego a una lista de precios
    for precios in precio_carrito: #recorro la lista de precios
        precio_total += precios #sumo iteradamente los percios
    return precio_total #retorno el precio total para usarlo más adelante

def agregar_items(nombre,precio,kcal,ingredientes): #funcion de agregar items
    nuevo_item = {"nombre":nombre,
                  "precio":precio,
                  "kcal":kcal,
                  "ingredientes":ingredientes}
    return nuevo_item #retorno el nuevo item para usar más adelante



         

    







