
millares = ["", "M", "MM", "MMM"]
centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
unidades = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
digitos_romanos = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
def convertir_en_romano(numero):
    
    if not isinstance(numero, int):
        return "No has introducido un número"
    if numero < 1 or numero > 3999:
        return "El número introducido no es válido (debe ser positivo y menor que 4000)"

    # continuamos con la conversión
    
    divisor = [1000, 100, 10, 1]
    
    factores = []
    for i in divisor:
        valor = numero // i
        numero = numero % i
        factores.append(valor)
    print(factores)
    r_millares = millares[factores[0]]
    r_centenas = centenas[factores[1]]
    r_decenas = decenas[factores[2]]
    r_unidades = unidades[factores[3]]
    return r_millares + r_centenas + r_decenas + r_unidades

def convertir_a_numero(romano):
    resultado = 0
    anterior = 0
    for letra in romano:
        actual = digitos_romanos[letra]
        if anterior >= actual: 
            resultado += actual
        else:
            resultado -= anterior #Deshaz la suma que hicimos en el anterior ciclo
            resultado += actual - anterior #suma la relacion entre los dos valores
        
        anterior = actual 
    return resultado

    

print("IX")
print(convertir_a_numero("IC"))
