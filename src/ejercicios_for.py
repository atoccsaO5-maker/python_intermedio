## 1. crear una lista de ingredientes ["camote","papa","queso","huevo"] crear un programa que recorra com for los elementos de la lista y me retorne el valor y su indice dled ingrediente "queso"
ingredientes = ["camote", "papa", "queso", "huevo"]

for indice, valor in enumerate(ingredientes):
  if valor == "queso":
    print(f"Índice: {indice}, Valor: {valor}")

## 2. del siguiente texto "errar es umano dio el pato bajandoce de la gallina" encontrar el error ortografico y corregirlo por el correcto.

texto = "errar es umano dio el pato bajandoce de la gallina"

for incorrecta, correcta in [("umano", "humano"), ("bajandoce", "bajándose")]:
  texto = texto.replace(incorrecta, correcta)

print(texto)









