# Búsqueda de Raíz de Función Cuadrática mediante el Método de Secante

## Descripción del Proyecto

Este script en Python implementa el **método de la secante** para encontrar una raíz de una función cuadrática de la forma \( f(x) = ax^2 + bx + c \). El método de la secante es un procedimiento iterativo que aproxima la raíz utilizando dos valores iniciales y se detiene cuando se cumple un criterio de convergencia definido por una tolerancia o cuando se alcanza el número máximo de iteraciones.

## Funcionalidad

El programa:
1. Solicita al usuario los coeficientes de la función cuadrática (`a`, `b`, `c`) y dos valores iniciales (`x0` y `x1`) para comenzar el proceso iterativo.
2. Itera el método de la secante, calculando los valores sucesivos de \( x \) hasta encontrar una raíz que cumpla con el criterio de convergencia.
3. Imprime la raíz encontrada y el número de iteraciones utilizadas.
4. Si no se encuentra una raíz dentro del número máximo de iteraciones, informa que el método no ha convergido.

