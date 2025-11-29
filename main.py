

import sys

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
    
    m_str = data[0].strip()  
    s = data[1]             
    # Intenta convertir la altura a entero
    try:
        # Convertir m_str a entero y asignarlo a m
        m = int(m_str)
    except ValueError:
        # Imprimir error y salir
        print("Error: La altura debe ser un numero entero")
        return
    
    # Validar que la altura sea positiva
    if m <= 0:
        print("Error: La altura debe ser un entero positivo")
        return
    
    # Validar que el carácter no esté vacío
    if len(s) == 0 or s.strip() == '':
        print("Error: El caracter no puede ser vacio")
        return
    
    # Llamar a la función reloj_arena con los parámetros m y s
    reloj_arena(m, s[0])

if __name__ == "__main__":
    main()



# ARCHIVO: solucion.py
# ============================================
def reloj_arena(m, s):
    """
    Construye y dibuja el reloj de arena.
    
    Parámetros:
    m: int - Número de líneas de la parte superior (altura), entero positivo
    s: str - Carácter para dibujar la figura
    
    La función asume que m es un entero positivo y s es un carácter válido.
    """
    # Dibujar la parte superior del reloj (triángulo decreciente)
    for i in range(m):
        espacios = ' ' * i
        caracteres = s * (2 * m - 1 - 2 * i)
        print(espacios + caracteres)
    
    # Dibujar la parte inferior del reloj (triángulo creciente)
    for i in range(m - 1):
        espacios = ' ' * (m - 2 - i)
        caracteres = s * (3 + 2 * i)
        print(espacios + caracteres)
