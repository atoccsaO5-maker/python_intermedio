# 1. Escriba un programa que acepte las opciones de dos jugadores en piedra-papel
# Entrada: persona1 = piedra, persona2 = papel
# Salida: gana persona2, papel envuelve piedra

opciones = ("piedra", "papel")

persona1 = input("Jugador 1, elige (piedra/papel): ").strip().lower()
persona2 = input("Jugador 2, elige (piedra/papel): ").strip().lower()

if persona1 not in opciones or persona2 not in opciones:
    print("Opcion invalida. Debe ser piedra o papel.")
elif persona1 == persona2:
    print("Empate")
elif persona1 == "piedra" and persona2 == "papel":
    print("Gana persona2, papel envuelve piedra")
elif persona1 == "papel" and persona2 == "piedra":
    print("Gana persona1, papel envuelve piedra")

# 2. Escriba un programa que acepte 3 numeros y calcule el minimo
# Entrada: 7, 4, 8
# Salida: 4

a = float(input("Numero 1: "))
b = float(input("Numero 2: "))
c = float(input("Numero 3: "))

minimo = a
if b < minimo:
    minimo = b
if c < minimo:
    minimo = c

print("El minimo es:", minimo)
