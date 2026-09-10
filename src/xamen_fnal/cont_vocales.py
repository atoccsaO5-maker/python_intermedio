# *Ejercicio CONT_VOCAL:* Contador de Vocales en un Texto (Bucle for y range)
# Pide al usuario que ingrese una frase o palabra. Utilizando un bucle for, recorre la cadena e
# imprime únicamente los números pares correspondiente a las posiciones/índices de los caracteres,
# junto con el carácter en dicha posición.
#
# Pista: Puedes combinar la función range() junto con len(texto) para iterar sobre los índices de la cadena.

texto = input("Ingresa una frase o palabra: ")

for indice in range(len(texto)):
    if indice % 2 == 0:
        print(f"Índice {indice}: {texto[indice]}")