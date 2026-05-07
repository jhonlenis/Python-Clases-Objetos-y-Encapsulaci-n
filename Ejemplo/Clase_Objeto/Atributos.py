# ==========================================
# TIPOS DE ATRIBUTOS EN PYTHON
# ==========================================

# 1. Atributos de Instancia vs Clase
class Estudiante:
    universidad = "Universidad Autónoma"  # Atributo de clase (compartido)

    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia
        self.activo = True    # Atributo de instancia con valor predeterminado

# 2. Visibilidad (Públicos, Protegidos y Privados)
class CuentaBancaria:
    tasa_interes = 0.03  # Atributo de clase público

    def __init__(self, titular, saldo_inicial, pin):
        self.titular = titular        # Público
        self._saldo = saldo_inicial   # Protegido (convención)
        self.__pin = pin              # Privado (name mangling)

    def verificar_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado

# 3. Propiedades (Getters, Setters y Validación)
class Temperatura:
    def __init__(self):
        self._celsius = 0

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("No puede ser menor que el cero absoluto")
        self._celsius = valor

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valor):
        self.celsius = (valor - 32) * 5/9

# 4. Atributos Calculados (Solo lectura)
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self):
        return self.ancho * self.alto

# 5. Atributos Especiales y Dinámicos
class Ejemplo:
    """Clase de ejemplo para mostrar atributos especiales"""
    def __init__(self, valor):
        self.valor = valor

# ==========================================
# PRUEBAS DE EJECUCIÓN
# ==========================================

if __name__ == "__main__":
    print("--- 1. Atributos de Clase e Instancia ---")
    e1 = Estudiante("María", 20)
    e2 = Estudiante("Carlos", 22)
    print(f"{e1.nombre} estudia en {e1.universidad}")
    
    Estudiante.universidad = "Universidad Complutense"
    print(f"Tras el cambio, {e2.nombre} estudia en {e2.universidad}\n")

    print("--- 2. Visibilidad ---")
    cuenta = CuentaBancaria("Ana López", 1000, "1234")
    print(f"Titular: {cuenta.titular}")
    print(f"Saldo (protegido): {cuenta._saldo}")
    # print(cuenta.__pin)  # Esto lanzaría un error
    print(f"PIN via mangling: {cuenta._CuentaBancaria__pin}\n")

    print("--- 3. Propiedades y Validación ---")
    t = Temperatura()
    t.celsius = 25
    print(f"Celsius: {t.celsius}°C | Fahrenheit: {t.fahrenheit}°F")
    try:
        t.celsius = -300
    except ValueError as e:
        print(f"Error capturado: {e}\n")

    print("--- 4. Atributos Calculados ---")
    r = Rectangulo(10, 5)
    print(f"Rectángulo 10x5 - Área: {r.area}")
    r.ancho = 20
    print(f"Rectángulo 20x5 - Área: {r.area}\n")

    print("--- 5. Funciones Integradas (hasattr, getattr) ---")
    p = Estudiante("Laura", 29)
    setattr(p, "apellido", "García") # Añadir dinámicamente
    if hasattr(p, "apellido"):
        print(f"Apellido encontrado: {getattr(p, 'apellido')}")
    
    print("\n--- 6. Atributos Especiales ---")
    obj = Ejemplo(42)
    print(f"Clase: {obj.__class__.__name__}")
    print(f"Docstring: {Ejemplo.__doc__}")
    print(f"Diccionario interno (__dict__): {obj.__dict__}")