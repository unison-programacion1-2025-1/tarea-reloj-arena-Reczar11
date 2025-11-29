def reloj_arena(m: int, s: str) -> str:
    # TODO: validar altura mayor que 0 e imprimir "Error: La altura debe ser un entero positivo" y salir
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return
    for i in range(m):
        num_espacios = i
        num_caracteres = 2 * m - 1 - 2 * i
        print(' ' * num_espacios + s * num_caracteres)
    
    # Dibujar la parte inferior del reloj (triángulo creciente) - m-1 líneas
    for i in range(m - 1):
        num_espacios = m - 2 - i
        num_caracteres = 3 + 2 * i
        print(' ' * num_espacios + s * num_caracteres)


# ============================================
# ARCHIVO: main.py
# ============================================
# Completa las validaciones y llama a la función
import sys
# Importar la función reloj_arena
from solucion import reloj_arena

def main():
    """
    data: lista de líneas leídas desde la entrada estándar o ingresadas por el usuario
          donde cada elemento de la lista es un string    
    """
    # IF que permite leer desde la entrada estándar o pedir datos al usuario
    if sys.stdin.isatty():
        data = []
        data.append(input("Ingresa la altura: ").strip())
        data.append(input("Ingresa el caracter: "))
    else:
        data = sys.stdin.read().strip().splitlines()
    
    # Validar que se recibieron dos líneas
    if len(data) < 2:
        print("Error: Se esperan 2 lineas de entrada (altura, caracter)")
        return
    
    m_str = data[0].strip()  # Primera línea: altura máxima (como texto)
    s = data[1]              # Segunda línea: carácter (o cadena) para la figura
    
    # Intentar convertir la altura a entero
    try:
        # Convertir m_str a entero y asignarlo a m
        m = int(m_str)
    except ValueError:
        # Imprimir error y salir
        print("Error: La altura debe ser un numero entero")
        return
    
    # Validar que el carácter no esté vacío
    if len(s) == 0:
        print("Error: El caracter no puede ser vacio")
        return
    
    # Llamar a la función reloj_arena con los parámetros m y primer carácter de s
    reloj_arena(m, s[0])

if __name__ == "__main__":
    main()
