"""
En esta ocasión realizaremos un programa que convierta temperatura, desde grados Fahrenheit a grados Celsius
y viceversa grados Celsius a grados Fahrenheit
"""
# Mensaje de bienvenida y pasos a seguir (impresión en pantalla)
print ("\n ******************************************")
print ("* Bienvenido al convertidor de temperatura *")
print (" ******************************************")
print ("\nIndicame que convertiremos.\n")

# Crearemos una variable opcion y lo inicializamos en 0 para posteriormente guardar la opción 
# escogida por el usuario del programa
opcion = 0

# Crearemos un ciclo “Mientras” con la condición de que hasta variable opción sella distinta de 1 y 2,
# (este fue el propósito de inicializar en 0 la variable opción, para que se active el ciclo mientras),
# que le pida al usuario a escoger una opción que quiere convertir:
# 1) Corresponde a Fahrenheit a Celsius
# 2) Corresponde a Celsius a Fahrenheit
# El (int) significa que el dato ingresado por el usuario tiene que ser de tipo entero.
while opcion != 1 and opcion != 2:
    opcion = int(input("Presiona 1 para Fahrenheit a Celsius o 2 para Celsius a Fahrenheit:\n"))
    
    # La instrucción Si se encargara de vigilar que el usuario no ingrese valores distintos
    # de 1 o 2 que le ofrecimos nosotros.
    # Y si tendremos un valor distinto de 1 y 2 imprimiremos por pantalla que la opción es incorrecta, que intente nuevamente.
    if opcion != 1 and opcion != 2:
        print ("\nOpcion incorrecta, intenta nuevamente\n")
        
    else: # A contrario de lo mencionado anteriormente se ejecutará lo siguiente:

        # Si la opción seleccionada es 1 se ejecutarán las siguientes instrucciones:
        # Creamos una variable (temp_fahr) que recibirá un dato de tipo float (real) cual seria ingresado por
        # el usuario después que imprimiremos por pantalla que nos indique la temperatura a convertir.
        # Segunda instrucción creamos una variable (resultado) que almacenara el valor de la expresión
        # matemática para convertir la temperatura desde Fahrenheit a Celsius.
        # La expresión matemática es lo siguiente: temperatura ingresada por el usuario le restamos 32
        # después multiplicamos por cinco dividido a nueve.
        # Se solucionan el paréntesis primero: 1) resta, 2) división y por último la multiplicación.
        # Imprimimos por pantalla que La temperatura en Celsius es y se monstrara el valor guardado
        # en variable resultado con un decimal.
        if opcion == 1:
            temp_fahr = float(input("\nIndica la temperatura en Fahrenheit: "))
            resultado = (temp_fahr - 32)*(5/9)
            print (f"\nLa temperatura en Celsius es: {resultado:.1f}")

        # Si la opción seleccionada es diferente de 1 se ejecutarán las siguientes instrucciones:
        # Creamos una variable (temp_cels) que recibirá un dato de tipo float (real) cual seria ingresado por
        # el usuario después que imprimiremos por pantalla que nos indique la temperatura a convertir.
        # Segunda instrucción reutilizamos la misma variable (resultado) que almacenara el valor de la expresión
        # matemática para convertir la temperatura desde Celsius a Fahrenheit.
        # La expresión matemática es lo siguiente: temperatura ingresada por el usuario lo multiplicamos por 9 dividido a 5 y le sumamos 32
        # 9 dividido a 5 y le sumamos 32.
        # Se solucionan el paréntesis primero: 1) división, 2) multiplicación y por último la suma.
        # Imprimimos por pantalla que La temperatura en Fahrenheit es y se monstrara el valor guardado
        # en variable resultado con un decimal.
        else:
            temp_cels = float(input("\nIndica la temperatura en Celsius: "))
            resultado = (temp_cels * (9/5)) + 32
            print (f"\nLa temperatura en Fahrenheit es: {resultado:.1f}")

# Al final ultima instrucción es impresión por pantalla del mensaje de agradecimiento.
print ("\nGracias por utilizar nuestro convertidor de temperatura")
