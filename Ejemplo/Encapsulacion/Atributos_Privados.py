# ==========================================
# ENCAPSULACIÓN Y ATRIBUTOS PRIVADOS
# ==========================================

# 1. Atributos "Protegidos" por convención (_)
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        # El guion bajo indica: "Por favor, no toques esto desde fuera"
        self._titular = titular
        self._saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

# 2. Atributos "Privados" con Name Mangling (__)
class CuentaSegura:
    def __init__(self, titular, saldo_inicial, pin):
        self._titular = titular
        self._saldo = saldo_inicial
        self.__pin = pin  # Realmente privado (Python le cambia el nombre)

    def validar_pin(self, pin_ingresado):
        return self.__pin == pin_ingresado

# 3. Encapsulación en Herencia (Protegidos vs Privados)
class Vehiculo:
    def __init__(self, marca, modelo):
        self._marca = marca      # Protegido: accesible por hijos
        self.__modelo = modelo   # Privado: solo para esta clase

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def mostrar_info(self):
        # Acceso al protegido (funciona)
        print(f"Marca: {self._marca}")
        
        # Acceso al privado del padre (fallará)
        try:
            print(f"Modelo: {self.__modelo}")
        except AttributeError:
            print("Error: No tengo acceso al atributo __modelo de mi padre.")

# 4. Validación de datos con atributos privados
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = precio

# ==========================================
# PRUEBAS DE EJECUCIÓN
# ==========================================

if __name__ == "__main__":
    print("--- 1. Convención de Guion Bajo (_) ---")
    cuenta_ana = CuentaBancaria("Ana García", 1000)
    print(f"Saldo (aunque sea _saldo): {cuenta_ana._saldo}")
    print("Nota: Acceder a _saldo es posible, pero rompe la convención.\n")

    print("--- 2. Doble Guion Bajo (__) y Name Mangling ---")
    cuenta_s = CuentaSegura("Carlos", 500, "9988")
    try:
        print(cuenta_s.__pin)
    except AttributeError:
        print("Atributo __pin no encontrado (está oculto)")
    
    # Revelando el truco de Python
    print(f"Acceso 'secreto': {cuenta_s._CuentaSegura__pin}\n")

    print("--- 3. Herencia y Visibilidad ---")
    mi_coche = Coche("Toyota", "Corolla", 4)
    mi_coche.mostrar_info()
    print("")

    print("--- 4. Validación en Constructor ---")
    try:
        p = Producto("Radio", -10)
    except ValueError as e:
        print(f"Validación exitosa: {e}")