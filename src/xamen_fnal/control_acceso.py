# *Ejercicio CONTROL_ACCESO:* Control de Acceso con Intentos (Bucle while y break)
# Escribe un programa que simule el acceso a una cuenta personal mediante una contraseña
# previamente definida (por ejemplo, "python123").
# - El usuario tiene un máximo de 3 intentos para ingresar la clave correcta.
# - Si ingresa la contraseña correcta, el programa debe mostrar "Acceso concedido" y terminar
#   inmediatamente con break.
# - Si se equivoca, debe mostrar cuántos intentos le quedan.
# - Si agota los 3 intentos sin éxito, debe imprimir "Cuenta bloqueada por seguridad".

clave_correcta: str = "python123"
intentos_maximos: int = 3
intentos: int = 0

while intentos < intentos_maximos:
    clave = input("Ingresa tu contraseña: ")
    intentos += 1

    if clave == clave_correcta:
        print("Acceso concedido")
        break

    intentos_restantes = intentos_maximos - intentos
    if intentos_restantes > 0:
        print(f"Contraseña incorrecta. Te quedan {intentos_restantes} intento(s).")
    else:
        print("Cuenta bloqueada por seguridad")