# ==========================================
# GETTERS Y SETTERS TRADICIONALES
# ==========================================

# 1. Ejemplo Base: Persona con validación simple
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Getter y Setter para nombre
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and len(nuevo_nombre) > 0:
            self._nombre = nuevo_nombre
        else:
            raise ValueError("El nombre debe ser una cadena no vacía")

    # Getter y Setter para edad
    def get_edad(self):
        return self._edad

    def set_edad(self, nueva_edad):
        if isinstance(nueva_edad, int) and 0 <= nueva_edad <= 120:
            self._edad = nueva_edad
        else:
            raise ValueError("La edad debe ser un entero entre 0 y 120")

# 2. Ejemplo Avanzado: Producto con lógica de descuento
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock
        self._descuento = 0

    def get_nombre(self): return self._nombre
    
    def get_precio(self):
        # El getter puede devolver un valor procesado (con descuento)
        return self._precio * (1 - self._descuento)

    def get_precio_base(self): return self._precio

    def get_stock(self): return self._stock

    def set_stock(self, nuevo_stock):
        if isinstance(nuevo_stock, int) and nuevo_stock >= 0:
            self._stock = nuevo_stock
        else:
            raise ValueError("El stock debe ser un entero positivo")

    def set_descuento(self, nuevo_descuento):
        if isinstance(nuevo_descuento, float) and 0 <= nuevo_descuento <= 1:
            self._descuento = nuevo_descuento
        else:
            raise ValueError("El descuento debe estar entre 0 y 1")

# 3. Ejemplo Herencia: Electrónico (Sobrescritura de Setters)
class Electronico(Producto):
    def __init__(self, nombre, precio, stock, garantia_meses):
        super().__init__(nombre, precio, stock)
        self._garantia_meses = garantia_meses
        self._activado = False

    def get_garantia(self): return self._garantia_meses

    def set_precio(self, nuevo_precio):
        # Usamos lógica del padre y añadimos propia
        if nuevo_precio < 0: raise ValueError("Precio inválido")
        self._precio = nuevo_precio
        if nuevo_precio > 1000:
            self._garantia_meses = max(self._garantia_meses, 24)
            print(f"¡Garantía extendida a {self._garantia_meses} meses por precio Premium!")

# ==========================================
# PRUEBAS DE FUNCIONAMIENTO
# ==========================================

if __name__ == "__main__":
    print("--- 1. Prueba Persona ---")
    ana = Persona("Ana López", 29)
    ana.set_edad(30)
    print(f"Nombre: {ana.get_nombre()}, Edad: {ana.get_edad()}")
    try:
        ana.set_edad(150)
    except ValueError as e:
        print(f"Validación edad: {e}\n")

    print("--- 2. Prueba Producto (Cálculos) ---")
    laptop = Producto("Laptop XPS", 1000.0, 5)
    laptop.set_descuento(0.10) # 10% descuento
    print(f"Precio Base: {laptop.get_precio_base()}")
    print(f"Precio con Descuento: {laptop.get_precio()}\n")

    print("--- 3. Prueba Herencia (Electrónico) ---")
    tv = Electronico("Smart TV", 800.0, 10, 12)
    print(f"Garantía inicial: {tv.get_garantia()} meses")
    tv.set_precio(1200.0) # Esto debería disparar la lógica extra
    print(f"Garantía final: {tv.get_garantia()} meses")