## usando while crear un programa que me de una pregunta para respomder y que solo tenga tres oportunidades para dar con la respuesta correcta

intentos: int = 0
respuesta_correcta: str = "python"

while intentos < 3:
    respuesta: str = input("¿Qué lenguaje de programación usa 'print' para mostrar en pantalla? ").lower()
    intentos += 1

    if respuesta == respuesta_correcta:
        print("¡Correcto!")
        break
    else:
        restantes: int = 3 - intentos
        if restantes > 0:
            print(f"Incorrecto. Te quedan {restantes} intento(s).")
        else:
            print("Incorrecto. Se acabaron tus intentos.")

print("Fin del programa.")