# ==========================================
# TALLER: ENCAPSULACIÓN (CuentaBancaria)
# ==========================================

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        """Inicializa la cuenta con un titular y un saldo base."""
        self._titular = titular
        
        # Usamos el setter de la propiedad para validar el saldo inicial
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        self._saldo = float(saldo_inicial)

    # --- PROPIEDAD TITULAR (Solo lectura) ---
    @property
    def titular(self):
        """Permite ver el nombre del titular pero no cambiarlo."""
        return self._titular

    # Al no definir @titular.setter, el atributo queda protegido contra escritura

    # --- PROPIEDAD SALDO (Lectura y Escritura con validación) ---
    @property
    def saldo(self):
        """Obtiene el saldo actual."""
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_valor):
        """Valida que el saldo nunca baje de cero."""
        if nuevo_valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = float(nuevo_valor)

    # --- MÉTODOS DE OPERACIÓN ---
    def depositar(self, cantidad):
        """Incrementa el saldo si la cantidad es válida."""
        if cantidad > 0:
            self.saldo += cantidad  # Usa el setter internamente
            return True
        return False

    def retirar(self, cantidad):
        """Disminuye el saldo si hay fondos suficientes."""
        if 0 < cantidad <= self._saldo:
            self.saldo -= cantidad  # Usa el setter internamente
            return True
        return False

# ==========================================
# PRUEBAS DEL TALLER
# ==========================================

if __name__ == "__main__":
    print("--- Creación de Cuenta ---")
    mi_cuenta = CuentaBancaria("Alejandro", 100.0)
    print(f"Cuenta de: {mi_cuenta.titular}")
    print(f"Saldo inicial: ${mi_cuenta.saldo}")

    print("\n--- Probando Restricción de Titular ---")
    try:
        mi_cuenta.titular = "Juan"  # Esto debe fallar
    except AttributeError as e:
        print(f"Éxito: {e} (No se puede modificar el titular)")

    print("\n--- Probando Depósitos y Retiros ---")
    if mi_cuenta.depositar(50):
        print(f"Depósito de $50 exitoso. Nuevo saldo: ${mi_cuenta.saldo}")
    
    if mi_cuenta.retirar(30):
        print(f"Retiro de $30 exitoso. Nuevo saldo: ${mi_cuenta.saldo}")
    
    if not mi_cuenta.retirar(200):
        print(f"Retiro de $200 rechazado: Fondos insuficientes (${mi_cuenta.saldo})")

    print("\n--- Probando Validación de Saldo Negativo ---")
    try:
        mi_cuenta.saldo = -10
    except ValueError as e:
        print(f"Error capturado correctamente: {e}")