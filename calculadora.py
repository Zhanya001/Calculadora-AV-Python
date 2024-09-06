import numpy as np
import sympy as sp
import unittest

# Función para validar entradas numéricas positivas
def validar_entrada_positiva(valor):
    """
    Verifica si el valor proporcionado es un número positivo mayor que cero.
    
    Parámetros:
    valor (int, float): El valor que se debe validar.

    Excepciones:
    TypeError: Se lanza si el valor no es un número.
    ValueError: Se lanza si el valor es menor o igual a cero.
    """
    if not isinstance(valor, (int, float)):
        raise TypeError("El valor debe ser un número.")
    if valor <= 0:
        raise ValueError("El valor debe ser mayor que cero.")

# Área círculo (numpy)
def area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Parámetros:
    radio (float): El radio del círculo. Debe ser un número positivo.

    Retorna:
    float: El área del círculo calculada como pi * radio^2.

    Excepciones:
    TypeError: Se lanza si el radio no es un número.
    ValueError: Se lanza si el radio es menor o igual a 0.
    """
    validar_entrada_positiva(radio)
    return np.pi * radio ** 2

# Área triángulo (sympy)
def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dada su base y altura.

    Parámetros:
    base (float): La base del triángulo. Debe ser un número positivo.
    altura (float): La altura del triángulo. Debe ser un número positivo.

    Retorna:
    float: El área del triángulo calculada como (base * altura) / 2.

    Excepciones:
    TypeError: Se lanza si base o altura no son números.
    ValueError: Se lanza si base o altura son menores o iguales a 0.
    """
    validar_entrada_positiva(base)
    validar_entrada_positiva(altura)
    
    base_sym, altura_sym = sp.symbols('base altura')
    area = (base_sym * altura_sym) / 2
    return area.subs({base_sym: base, altura_sym: altura})

# Área cuadrado (numpy)
def area_cuadrado(lado):
    """
    Calcula el área de un cuadrado dado el lado.

    Parámetros:
    lado (float): El lado del cuadrado. Debe ser un número positivo.

    Retorna:
    float: El área del cuadrado calculada como lado^2.

    Excepciones:
    TypeError: Se lanza si el lado no es un número.
    ValueError: Se lanza si el lado es menor o igual a 0.
    """
    validar_entrada_positiva(lado)
    return lado ** 2

# Volumen cubo (numpy)
def volumen_cubo(lado):
    """
    Calcula el volumen de un cubo dado su lado.

    Parámetros:
    lado (float): El lado del cubo. Debe ser un número positivo.

    Retorna:
    float: El volumen del cubo calculado como lado^3.

    Excepciones:
    TypeError: Se lanza si el lado no es un número.
    ValueError: Se lanza si el lado es menor o igual a 0.
    """
    validar_entrada_positiva(lado)
    return lado ** 3

# Área de un rectángulo
def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo dada su base y altura.

    Parámetros:
    base (float): La base del rectángulo. Debe ser un número positivo.
    altura (float): La altura del rectángulo. Debe ser un número positivo.

    Retorna:
    float: El área del rectángulo calculada como base * altura.

    Excepciones:
    TypeError: Se lanza si la base o la altura no son números.
    ValueError: Se lanza si la base o la altura son menores o iguales a 0.
    """
    validar_entrada_positiva(base)
    validar_entrada_positiva(altura)
    return base * altura

# Pruebas unitarias
class TestGeometria(unittest.TestCase):

    def test_area_circulo(self):
        self.assertAlmostEqual(area_circulo(5), np.pi * 25)
        with self.assertRaises(ValueError):
            area_circulo(-1)
        with self.assertRaises(TypeError):
            area_circulo("5")

    def test_area_triangulo(self):
        self.assertEqual(area_triangulo(3, 4), 6)
        with self.assertRaises(ValueError):
            area_triangulo(0, 4)
        with self.assertRaises(TypeError):
            area_triangulo(3, "altura")

    def test_area_cuadrado(self):
        self.assertEqual(area_cuadrado(2), 4)
        with self.assertRaises(ValueError):
            area_cuadrado(-2)
        with self.assertRaises(TypeError):
            area_cuadrado("lado")

    def test_volumen_cubo(self):
        self.assertEqual(volumen_cubo(2), 8)
        with self.assertRaises(ValueError):
            volumen_cubo(-2)
        with self.assertRaises(TypeError):
            volumen_cubo("lado")

    def test_area_rectangulo(self):
        self.assertEqual(area_rectangulo(5, 3), 15)
        with self.assertRaises(ValueError):
            area_rectangulo(0, 3)
        with self.assertRaises(TypeError):
            area_rectangulo("5", 3)

# Mostrar instrucciones
def mostrar_instrucciones():
    
    print("\n" + "="*60)
    print(" " * 15 + "🔢 Instrucciones de Uso 🔢")
    print("="*60)
    print("🔵 Área de un círculo:")
    print("   ➡  El radio debe ser un número positivo mayor que 0.")
    print("   🚫 No se permiten valores negativos ni cero.")
    print("-" * 60)
    
    print("🔺 Área de un triángulo:")
    print("   ➡  La base y la altura deben ser números positivos mayores que 0.")
    print("   🚫 No se permiten valores negativos ni cero.")
    print("-" * 60)
    
    print("🟩 Área de un cuadrado:")
    print("   ➡  El lado debe ser un número positivo mayor que 0.")
    print("   🚫 No se permiten valores negativos ni cero.")
    print("-" * 60)
    
    print("🟦 Volumen de un cubo:")
    print("   ➡  El lado debe ser un número positivo mayor que 0.")
    print("   🚫 No se permiten valores negativos ni cero.")
    print("-" * 60)
    
    print("🟧 Área de un rectángulo:")
    print("   ➡  La base y la altura deben ser números positivos mayores que 0.")
    print("   🚫 No se permiten valores negativos ni cero.")
    print("="*60 + "\n")
    
# Función principal para solicitar valores del usuario
def solicitar_valores():
    while(True):
        try:
        
            print("\n--- Calculadora Geométrica ---\n")
            # Preguntar al usuario qué cálculo desea hacer
            print("1. Área de un círculo")
            print("2. Área de un triángulo")
            print("3. Área de un cuadrado")
            print("4. Volumen de un cubo")
            print("5. Área de un rectángulo")
            print("6. Correr Unit Tests con unittest")
            print("7. Salir del programa")
            opcion = int(input("\nElige una opción (1-7): "))
            
            if opcion == 1:
                radio = input("Ingresa el radio del círculo: ")
                if not radio.isnumeric():
                    raise ValueError("El valor introducido no es un número")
                radio = float(radio)
                print(f"Área del círculo: {area_circulo(radio)}")
            elif opcion == 2:
                base = float(input("Ingresa la base del triángulo: "))
                altura = float(input("Ingresa la altura del triángulo: "))
                print(f"Área del triángulo: {area_triangulo(base, altura)}")
            elif opcion == 3:
                lado = float(input("Ingresa el lado del cuadrado: "))
                print(f"Área del cuadrado: {area_cuadrado(lado)}")
            elif opcion == 4:
                lado = float(input("Ingresa el lado del cubo: "))
                print(f"Volumen del cubo: {volumen_cubo(lado)}")
            elif opcion == 5:
                base = float(input("Ingresa la base del rectángulo: "))
                altura = float(input("Ingresa la altura del rectángulo: "))
                print(f"Área del rectángulo: {area_rectangulo(base, altura)}")
            elif opcion == 6:
                unittest.main(argv=[''], exit=False)
            elif opcion == 7:
                break
            else:
                print("Opción no válida. Elige un número entre 1 y 7.")

        except ValueError as e:
            print(f"Error: {e}. Asegúrate de ingresar un número válido.")
        except (TypeError, ValueError) as e:
            print(f"Error: {e}")

# Ejemplos y ejecución de la calculadora
if __name__ == "__main__":
    mostrar_instrucciones()
    solicitar_valores()