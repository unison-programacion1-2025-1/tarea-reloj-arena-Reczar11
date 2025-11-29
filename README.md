[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/LtSkrJzm)
# Tarea: ASCII Reloj de arena centrado

## 🎯 Objetivo
Practicar:
- Validación básica de datos de entrada.
- Uso de ciclos anidados (o múltiples ciclos) para generar patrones de texto.
- Manejo de lógica para imprimir espacios y caracteres en cada línea.
- Separación de responsabilidades entre lectura/validación de entrada y lógica del algoritmo.

## 📝 Descripción del Problema
Crear un programa que lea un número entero positivo `m`, que representa el número de líneas de la parte superior del reloj, y un carácter `s`.

El programa deberá dibujar una figura simétrica y centrada de la siguiente manera:

1. Primero, dibujará un triángulo decreciente (la parte superior del reloj) de `m` líneas.
   - La primera línea tendrá $2*m - 1$ caracteres `s` (y 0 espacios).
   - La última línea de esta parte (la punta) tendrá $1$ carácter `s` (y $m - 1$ espacios).

2. Inmediatamente después, dibujará un triángulo creciente (la parte inferior) de $m - 1$ líneas.
   - Comenzará con 3 caracteres `s` (y $m - 2$ espacios).
   - Terminará con $2*m - 1$ caracteres `s` (y 0 espacios).


Cada fila de la figura estará formada por una cantidad de espacios seguidos por una cantidad de caracteres `s`.

Si la entrada no cumple con las condiciones, el programa deberá mostrar el mensaje de error correspondiente y no dibujar la figura.

### 📥 Entrada
El programa recibirá dos líneas de entrada desde la entrada estándar:
1. Altura máxima (`m`):
   
   Una cadena que se espera que represente un número entero. Tras validarse, será el número de líneas de la parte superior del reloj y determinará el ancho máximo ($2*m - 1$).

2. Carácter (`s`):

   Una cadena de texto cuyo primer carácter se utilizará para rellenar la figura. Esta línea no puede estar vacía.

### 📤 Salida
Si la entrada es válida, el programa imprimirá por pantalla la figura simétrica y centrada:
- Primero, `m` líneas decrecientes.
- Después, $m - 1$ líneas crecientes.

Si la entrada es inválida, el programa imprimirá únicamente uno de los siguientes mensajes:

- Si no se reciben al menos 2 líneas:
   ```
   Error: Se esperan 2 lineas de entrada (altura, caracter)
   ```

- Si la primera línea no es un entero:
   ```
   Error: La altura debe ser un numero entero
   ```

- Si la altura es menor o igual a 0:
   ```
   Error: La altura debe ser un entero positivo
   ```

### ⛔️ Restricciones
- El programa debe trabajar únicamente con la entrada estándar (no debe pedir datos con input() dentro de la versión que se evalúa).
- No cambies los nombres de los archivos ni de la función reloj_arena

> (*Sugerencia*) Primero valida toda la entrada. Para la figura, calcula cuántos espacios necesitas imprimir antes del carácter `s` en cada línea. El número de espacios y el número de caracteres `s` cambiarán en cada fila.

### 🧾 Muestras
A continuación se muestran algunos ejemplos de entradas y salidas esperadas.

| Entrada | Salida |
|---------|--------|
| 5<br>* |  ********* <br> &nbsp; ******* <br> &nbsp; &nbsp; ***** <br> &nbsp; &nbsp; &nbsp; ***  <br> &nbsp; &nbsp; &nbsp; &nbsp; * <br> &nbsp; &nbsp; &nbsp; *** <br> &nbsp; &nbsp; ***** <br> &nbsp; ******* <br> ********* <br> |
| 3<br># | ##### <br> &nbsp; ### <br> &nbsp;&nbsp;&nbsp; # <br> &nbsp; ### <br> ##### <br> |
| 0<br>+ | Error: La altura debe ser un entero positivo |
| dos<br>@ | Error: La altura debe ser un numero entero |
| 5<br> | Error: El caracter no puede ser vacío |

El formato es estricto: respeta mayúsculas, minúsculas, espacios y saltos de línea.

### 🛠️ Resumen
- En **main.py**, valida primero todo lo relacionado con la entrada (cantidad de líneas, tipo de dato, vacío o no).
- En **solucion.py**, asume que s ya es válido y concéntrate en validar m y construir la figura (incluyendo los espacios y los caracteres).

---

## 📂 Estructura del Repositorio

```
.
├── README                        # Instrucciones de la tarea [No modificar]
├── main.py                       # Archivo para ejecutar el programa [No modificar]
├── solucion.py                   # Archivo donde debes implementar tu solución [Modificar]
├── .gitignore                    # Archivo para ignorar archivos en Git [No modificar]
├── requirements.txt              # Archivo para dependencias [No modificar]
└── disparador_autoevaluacion.py  # Archivo de respaldo para disparar la autoevaluación [No modificar]
```