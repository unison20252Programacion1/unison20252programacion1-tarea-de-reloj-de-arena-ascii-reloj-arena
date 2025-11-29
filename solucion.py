# En este archivo debes implementar la función

def reloj_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    try:
        if m<5:
            print("Error: La altura debe ser un entero positivo")
            return
    # TODO: implementar la lógica para generar el reloj de arena en ASCII
    for i in range(m//2 +1):
    print(" " * i + simbolo * (m - 2 * i))
for i in range(m//2 -1, -1, -1):
    print(" " * i + simbolo * (m - 2 * i))
