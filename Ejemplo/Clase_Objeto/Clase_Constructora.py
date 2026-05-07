# ==========================================
# EJEMPLOS DE CONSTRUCTORES EN PYTHON
# ==========================================

# 1. Clase Básica (Persona)
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# 2. Clase con Valores Predeterminados (Producto)
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

# 3. Inicialización con Cálculos (Rectangulo)
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.area = ancho * alto
        self.perimetro = 2 * (ancho + alto)

# 4. Constructor con Validación (Cuenta)
class Cuenta:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        self.saldo = saldo_inicial

# 5. Ejemplo Práctico: Biblioteca (Libro)
class Libro:
    def __init__(self, titulo, autor, paginas, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.isbn = isbn
        self.disponible = disponible
        self.pagina_actual = 0

# 6. Constructores Alternativos (@classmethod)
class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    @classmethod
    def desde_texto(cls, texto):
        dia, mes, año = map(int, texto.split('-'))
        return cls(dia, mes, año)

    @classmethod
    def hoy(cls):
        import datetime
        f = datetime.date.today()
        return cls(f.day, f.month, f.year)

# ==========================================
# EJECUCIÓN DE PRUEBAS
# ==========================================

if __name__ == "__main__":
    print("--- 1. Persona ---")
    ana = Persona("Ana García", 28)
    juan = Persona("Juan López", 35)
    print(f"{ana.nombre}: {ana.edad} años")
    print(f"{juan.nombre}: {juan.edad} años\n")

    print("--- 2. Producto ---")
    laptop = Producto("Laptop XPS", 1200)
    teclado = Producto("Teclado mecánico", 80, 15)
    print(f"{laptop.nombre} stock: {laptop.stock}")
    print(f"{teclado.nombre} stock: {teclado.stock}\n")

    print("--- 3. Rectangulo ---")
    rect = Rectangulo(5, 3)
    print(f"Área: {rect.area}, Perímetro: {rect.perimetro}\n")

    print("--- 4. Cuenta (Validación) ---")
    try:
        cuenta_error = Cuenta("Juan López", -500)
    except ValueError as e:
        print(f"Error esperado: {e}\n")

    print("--- 5. Libro ---")
    libro1 = Libro("Python Crash Course", "Eric Matthes", 544, "9781593279288")
    print(f"{libro1.titulo} está {'disponible' if libro1.disponible else 'prestado'}\n")

    print("--- 6. Fecha (Constructores Alternativos) ---")
    f1 = Fecha(15, 3, 2023)
    f2 = Fecha.desde_texto("25-12-2023")
    f3 = Fecha.hoy()
    print(f"Fecha normal: {f1.dia}/{f1.mes}/{f1.año}")
    print(f"Desde texto: {f2.dia}/{f2.mes}/{f2.año}")
    print(f"Hoy: {f3.dia}/{f3.mes}/{f3.año}")