# main.py
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
        entrada = sys.stdin.read().strip()
        data = entrada.splitlines()
    
    # Validar que se recibieron dos líneas
    if len(data) < 2:
        print("Error: Se esperan 2 lineas de entrada (altura, caracter)")
        return
    
    m_str = data[0].strip()  # Primera línea: altura máxima (como texto)
    
    # Segunda línea: carácter (sin hacer strip para preservar espacios)
    if len(data) > 1:
        s = data[1]
    else:
        s = ""
    
    # Intentar convertir la altura a entero
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
    if len(s) == 0:
        print("Error: El caracter no puede ser vacio")
        return
    
    # Llamar a la función reloj_arena con los parámetros m y primer carácter de s
    reloj_arena(m, s[0])

if __name__ == "__main__":
    main()
