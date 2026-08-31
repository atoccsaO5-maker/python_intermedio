
# Control de flujo

## Condicionales

### La sentencia if

La sentencia `if` permite ejecutar un bloque de codigo solo si se cumple una condicion. Es la base del control de flujo condicional en Python.

Sintaxis basica:

```python
if condicion:
    # bloque que se ejecuta si la condicion es verdadera
    instruccion1
    instruccion2
```

- La condicion es una expresion que se evalúa como `True` o `False`.
- El bloque de codigo debe estar indentado (con sangria de 4 espacios por convencion).

Variantes:

```python
# if con else
if condicion:
    print("Condicion verdadera")
else:
    print("Condicion falsa")

# if con elif (else if) encadenado
if a > b:
    print("a es mayor")
elif a < b:
    print("b es mayor")
else:
    print("a y b son iguales")
```

Operadores de comparacion: `==`, `!=`, `<`, `>`, `<=`, `>=`

Operadores logicos: `and`, `or`, `not`

Comprobar pertenencia: `in`, `not in`

## Repetitivas

## Funciones

## Manejo de excepciones

## Clases y objetos
