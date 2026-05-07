# ==========================================
# TALLER: CLASE LIBRO
# ==========================================

class Libro:
    def __init__(self, titulo, autor, paginas):
        """Constructor que inicializa los atributos básicos."""
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = True  # Inicialmente disponible

    def prestar(self):
        """Cambia la disponibilidad a False si es posible."""
        if self.disponible:
            self.disponible = False
            return f"El libro '{self.titulo}' ha sido prestado con éxito."
        else:
            return f"Lo sentimos, el libro '{self.titulo}' no está disponible actualmente."

    def devolver(self):
        """Cambia la disponibilidad a True si el libro estaba prestado."""
        if not self.disponible:
            self.disponible = True
            return f"El libro '{self.titulo}' ha sido devuelto."
        else:
            return f"El libro '{self.titulo}' ya se encontraba en la biblioteca."

    def informacion(self):
        """Devuelve un resumen completo del objeto."""
        estado = "Disponible" if self.disponible else "Prestado"
        return (f"LIBRO: {self.titulo}\n"
                f"Autor: {self.autor}\n"
                f"Páginas: {self.paginas}\n"
                f"Estado: {estado}\n"
                f"{'-' * 30}")

# ==========================================
# PRUEBAS DEL TALLER
# ==========================================

if __name__ == "__main__":
    # 1. Crear dos objetos diferentes
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)
    libro2 = Libro("1984", "George Orwell", 328)

    print("--- INFORMACIÓN INICIAL ---")
    print(libro1.informacion())
    print(libro2.informacion())

    print("\n--- PROBANDO PRESTAMOS ---")
    # Prestar libro 1
    print(libro1.prestar())
    # Intentar prestar libro 1 de nuevo (debe fallar)
    print(libro1.prestar())

    print("\n--- PROBANDO DEVOLUCIONES ---")
    # Devolver libro 1
    print(libro1.devolver())
    # Intentar devolver libro 2 (que ya estaba disponible)
    print(libro2.devolver())

    print("\n--- ESTADO FINAL ---")
    print(libro1.informacion())
    print(libro2.informacion())