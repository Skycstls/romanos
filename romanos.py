def convertir_en_romano(numero):
    """
    Restricciones:
        - Es un número natural
        - El número está entre 0 y 3999
            - no es negativo
            - no es mayor que 3999
    Resultado es una cadena que contiene (I, V, X, L, C, D, M)
    Ideas para comprobar un entero:
            - (X) isdigit(): porque no aplica a cualquier cosa que no sea cadena
        - (V) convertir a int y si no se puede, error
        - (V) isinstance()
            - (V) type()
            - (X) isnumeric()
    Pasos:
        1. Validar la entrada
        2a. Si es válido: lo convierto
        2b. Si no es válido: muestro un error
    """

    if not isinstance(numero, int):
        return "No has introducido un número"
    if numero < 1 or numero > 3999:
        return "El número introducido no es válido (debe ser positivo y menor que 4000)"

    # continuamos con la conversión
    simbolos = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    n_string = str(numero)
    n_list = list(n_string)
    print(n_list)
    int_list = []
    for num in n_list:
        n_int = int(num)
        int_list.append(n_int)
    
    resultado_str = ""
    if len(n_list) == 1:
        print("u")
        #[0] = unidades
    if len(n_list) == 2:
        print("d")
        #[0] = decenas
        #[1] = unidades
    if len(n_list) == 3:
        print("c")
        #[0] = centenas
        #[1] = decenas
        #[2] = unidades
    if len(n_list) == 4:
        print("m")
        
        #[0] = millares
        #[1] = centenas
        #[2] = decenas
        #[3] = unidades
        
        resultado_str += int_list[0]*"M"
        resultado_str += int_list[1]*"C"
        resultado_str += int_list[2]*"D"
    print(resultado_str)
    # Descomponer "numero" en unidades, decenas, centenas y unidades de millar
    # opción 1: división entera + módulo en cascada
    # opción 2: convertir en cadena y en función de la longitud y la posición obtener u,d,c y um

print(convertir_en_romano(1123))
# convertir_en_romano("a")