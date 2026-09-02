# crear un programa de login que mientras que la persona no ponga el usuario/contraseña correcto le siga pidiendo esa informacion
# si el usuario/contraseña son correctos entonces darle un mensaje de bienvenida y salir del programa

usuario_correcto: str = "admin"
contraseña_correcta: str = "1234"

usuario: str = ""
contraseña: str = ""

while usuario != usuario_correcto or contraseña != contraseña_correcta:
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print("¡Bienvenido!")
    else:
        print("Usuario o contraseña incorrectos. Intenta de nuevo.")

print("Saliendo del programa.")
