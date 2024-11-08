import math

tol = 1e-6  # Tolerancia para la convergencia
maxiterac = 100  # Máximo de iteraciones permitidas
countiter = 0  # Contador de iteraciones

# Coeficientes de la función cuadrática
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

# Valores iniciales
x0 = float(input("Ingrese el valor inicial x0: "))
x1 = float(input("Ingrese el valor inicial x1: "))

# Bucle para iterar el método
while countiter < maxiterac:
    fx0 = a * x0 ** 2 + b * x0 + c
    fx1 = a * x1 ** 2 + b * x1 + c
    
    
    
    # Calcula el siguiente valor x2
    x2 = x1 - (fx1 * (x1 - x0) / (fx1 - fx0))
    
    # Verifica si la solución ha convergido
    if abs(x2 - x1) < tol:
        x2 = round(x2, 2)
        print(f"Raíz encontrada: {x2:.2f} después de {countiter + 1} iteraciones.")
        break
    else:
        x0 = x1
        x1 = x2
        countiter += 1

# Mensaje si no se encuentra una raíz dentro del máximo de iteraciones
if countiter == maxiterac:
    print("El método no convergió después del número máximo de iteraciones.")


