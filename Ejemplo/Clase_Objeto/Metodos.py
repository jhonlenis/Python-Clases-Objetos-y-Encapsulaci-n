# ==========================================
# MÉTODOS EN PYTHON: COMPORTAMIENTO Y ACCIÓN
# ==========================================

# 1. Métodos de Instancia Básicos (Coche)
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        self.encendido = False
        self.velocidad_maxima = 200

    def encender(self):
        if not self.encendido:
            self.encendido = True
            return f"{self.marca} {self.modelo} encendido"
        return f"{self.marca} {self.modelo} ya estaba encendido"

    def apagar(self):
        if self.encendido:
            self.encendido = False
            self.velocidad = 0
            return f"{self.marca} {self.modelo} apagado"
        return f"{self.marca} {self.modelo} ya estaba apagado"

    def acelerar(self, incremento):
        if not self.encendido:
            return f"No se puede acelerar: {self.marca} {self.modelo} está apagado"
        nueva_velocidad = self.velocidad + incremento
        if nueva_velocidad > self.velocidad_maxima:
            self.velocidad = self.velocidad_maxima
            return f"Velocidad máxima alcanzada: {self.velocidad} km/h"
        self.velocidad = nueva_velocidad
        return f"Velocidad actual: {self.velocidad} km/h"

    def frenar(self, decremento):
        if self.velocidad == 0:
            return "El coche ya está detenido"
        nueva_velocidad = self.velocidad - decremento
        if nueva_velocidad < 0:
            self.velocidad = 0
            return "Coche detenido"
        self.velocidad = nueva_velocidad
        return f"Velocidad actual: {self.velocidad} km/h"

# 2. Métodos que interactúan con atributos (CuentaBancaria)
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial

    def consultar_saldo(self):
        return f"Saldo actual de {self.titular}: ${self._saldo}"

    def depositar(self, cantidad):
        if cantidad <= 0:
            return "La cantidad a depositar debe ser positiva"
        self._saldo += cantidad
        return f"Depósito de ${cantidad} realizado. Nuevo saldo: ${self._saldo}"

    def retirar(self, cantidad):
        if cantidad <= 0:
            return "La cantidad a retirar debe ser positiva"
        if cantidad > self._saldo:
            return "Fondos insuficientes"
        self._saldo -= cantidad
        return f"Retiro de ${cantidad} realizado. Nuevo saldo: ${self._saldo}"

# 3. Métodos con lógica y retornos complejos (Calculadora)
class Calculadora:
    def sumar(self, a, b): return a + b
    def dividir(self, a, b):
        return a / b if b != 0 else "Error: División por cero"

    def calcular_estadisticas(self, numeros):
        if not numeros:
            return {"suma": 0, "promedio": 0}
        return {
            "suma": sum(numeros),
            "promedio": sum(numeros) / len(numeros),
            "minimo": min(numeros),
            "maximo": max(numeros)
        }

# 4. Métodos que llaman a otros (Persona)
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def presentarse(self):
        estado = "mayor" if self.es_mayor_de_edad() else "menor"
        return f"Hola, soy {self.nombre_completo()} y soy {estado} de edad."

# 5. Métodos Especiales (Dunder Methods)
class Punto:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __str__(self): return f"({self.x}, {self.y})"
    
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

# 6. Métodos Estáticos y de Clase (MathUtils y Empleado)
class MathUtils:
    @staticmethod
    def factorial(n):
        if n == 0 or n == 1: return 1
        return n * MathUtils.factorial(n - 1)

class Empleado:
    num_empleados = 0
    def __init__(self, nombre, salario):
        self.nombre, self.salario = nombre, salario
        Empleado.num_empleados += 1
    
    @classmethod
    def obtener_total(cls): return cls.num_empleados

# ==========================================
# PRUEBAS DE LOS MÉTODOS
# ==========================================

if __name__ == "__main__":
    print("--- 1. Pruebas de Coche ---")
    mi_coche = Coche("Toyota", "Corolla")
    print(mi_coche.encender())
    print(mi_coche.acelerar(50))
    print(mi_coche.frenar(20), "\n")

    print("--- 2. Pruebas de CuentaBancaria ---")
    cuenta = CuentaBancaria("Ana López", 1000)
    print(cuenta.depositar(500))
    print(cuenta.retirar(2000), "\n")

    print("--- 3. Pruebas de Calculadora ---")
    calc = Calculadora()
    stats = calc.calcular_estadisticas([4, 7, 2, 9, 5])
    print(f"Estadísticas: {stats}\n")

    print("--- 4. Pruebas de Persona (Autoreferencia) ---")
    persona = Persona("Juan", "Pérez", 25)
    print(persona.presentarse(), "\n")

    print("--- 5. Pruebas de Métodos Especiales ---")
    p1, p2 = Punto(3, 4), Punto(1, 2)
    print(f"Suma de puntos: {p1 + p2}\n")

    print("--- 6. Pruebas Estáticas y de Clase ---")
    print(f"Factorial de 5: {MathUtils.factorial(5)}")
    e1 = Empleado("Ana", 3000)
    print(f"Total empleados: {Empleado.obtener_total()}")