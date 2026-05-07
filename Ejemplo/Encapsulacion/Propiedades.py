# ==========================================
# PROPIEDADES EN PYTHON (@property)
# ==========================================
import math

# 1. Ejemplo Clásico: Conversión y Validación (Temperatura)
class Temperatura:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        """Obtiene la temperatura en grados Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("No puede ser menor que el cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        """Calcula fahrenheit on-the-fly."""
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        celsius_calc = (valor - 32) * 5/9
        if celsius_calc < -273.15:
            raise ValueError("No puede ser menor que el cero absoluto")
        self._celsius = celsius_calc

# 2. Uso de Deleter y Protección de Listas (Persona)
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre
        self._amigos = []

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor:
            raise ValueError("Nombre inválido")
        self._nombre = valor

    @property
    def amigos(self):
        # Devolvemos copia para que no modifiquen la original sin permiso
        return self._amigos.copy()

    @amigos.deleter
    def amigos(self):
        self._amigos = []
        print("-> Lista de amigos vaciada.")

# 3. Propiedades de Solo Lectura y Calculadas (Círculo y Empleado)
class Circulo:
    def __init__(self, radio):
        self.radio = radio # Esto usa el setter automáticamente

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        if valor <= 0: raise ValueError("Radio debe ser positivo")
        self._radio = valor

    @property
    def area(self):
        return math.pi * self._radio ** 2

class Empleado:
    def __init__(self, nombre, salario_base, horas_extra=0, tarifa_extra=0):
        self.nombre = nombre
        self.salario_base = salario_base
        self.horas_extra = horas_extra
        self.tarifa_extra = tarifa_extra

    @property
    def salario_total(self):
        return self.salario_base + (self.horas_extra * self.tarifa_extra)

# 4. Herencia con Propiedades
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    @property
    def info(self):
        return f"{self._nombre}: {self._precio}€"

class ProductoDigital(Producto):
    def __init__(self, nombre, precio, tamaño_mb):
        super().__init__(nombre, precio)
        self.tamaño_mb = tamaño_mb

    @property
    def info(self): # Sobrescribimos la propiedad
        return f"{super().info} ({self.tamaño_mb} MB)"

# ==========================================
# PRUEBAS DE EJECUCIÓN
# ==========================================

if __name__ == "__main__":
    print("--- 1. Temperatura (Getter/Setter Pro) ---")
    t = Temperatura(25)
    t.fahrenheit = 68 
    print(f"68°F son {t.celsius}°C\n")

    print("--- 2. Persona (Setter y Deleter) ---")
    p = Persona("Carlos")
    p.nombre = "Carlos R."
    # Intentar modificar lista directamente no funcionará por el .copy()
    p.amigos.append("Ana") 
    print(f"Amigos de {p.nombre}: {p.amigos}") # Imprime []
    del p.amigos
    print("")

    print("--- 3. Propiedades Calculadas ---")
    c = Circulo(5)
    print(f"Área círculo r=5: {c.area:.2f}")
    
    emp = Empleado("Laura", 2000, 10, 20)
    print(f"Salario total {emp.nombre}: {emp.salario_total}€\n")

    print("--- 4. Herencia de Propiedades ---")
    ebook = ProductoDigital("Ebook Python", 19.99, 15)
    print(ebook.info)