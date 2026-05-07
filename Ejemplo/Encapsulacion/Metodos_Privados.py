# ==========================================
# MÉTODOS PRIVADOS Y PROTEGIDOS EN PYTHON
# ==========================================
import hashlib
import re
import math

# 1. Ejemplo Base: Seguridad (Autenticador)
class Autenticador:
    def __init__(self, usuario, contraseña):
        self._usuario = usuario
        # Llamada a un método "realmente" privado (__ con name mangling)
        self._contraseña_hash = self.__generar_hash(contraseña)

    def __generar_hash(self, contraseña):
        """Helper interno: el usuario no necesita saber CÓMO se hashea."""
        return hashlib.sha256(contraseña.encode()).hexdigest()

    def verificar_contraseña(self, contraseña_ingresada):
        """Interfaz pública: el usuario solo pregunta si es correcta."""
        return self.__generar_hash(contraseña_ingresada) == self._contraseña_hash

# 2. Ejemplo: Algoritmo por Etapas (ProcesadorTexto)
class ProcesadorTexto:
    def __init__(self):
        self._texto = ""
        self._estadisticas = {}

    def procesar(self, contenido):
        """Coordina la limpieza y el análisis mediante métodos privados."""
        self._texto = self.__normalizar(contenido)
        self._estadisticas = self.__analizar(self._texto)

    def __normalizar(self, texto):
        texto = texto.lower()
        return re.sub(r'[^\w\s]', '', texto).strip()

    def __analizar(self, texto):
        palabras = texto.split()
        return {
            'total': len(palabras),
            'unicas': len(set(palabras))
        }

    def obtener_resumen(self):
        return self._estadisticas

# 3. Métodos Protegidos para Herencia (Forma)
class Forma:
    def _validar_positivo(self, valor):
        """Método protegido: accesible para hijos, no recomendado para externos."""
        if valor <= 0: raise ValueError("Debe ser positivo")
        return True

class Circulo(Forma):
    def __init__(self, radio):
        self._validar_positivo(radio) # Reutilizando método del padre
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2

# 4. Validación Compleja Modular (Formulario)
class Formulario:
    def __init__(self):
        self.errores = {}

    def validar(self, datos):
        self.errores = {}
        # Dividimos una tarea grande en piezas pequeñas privadas
        self.__validar_email(datos.get('email', ''))
        self.__validar_pass(datos.get('pass', ''))
        return len(self.errores) == 0

    def __validar_email(self, email):
        if "@" not in email:
            self.errores['email'] = "Email inválido"

    def __validar_pass(self, password):
        if len(password) < 6:
            self.errores['pass'] = "Demasiado corta"

# ==========================================
# PRUEBAS DE FUNCIONAMIENTO
# ==========================================

if __name__ == "__main__":
    print("--- 1. Autenticador (Name Mangling) ---")
    auth = Autenticador("admin", "12345")
    print(f"¿Password correcto?: {auth.verificar_contraseña('12345')}")
    try:
        auth.__generar_hash("123") # Esto fallará
    except AttributeError:
        print("Éxito: No se puede acceder a __generar_hash desde fuera.\n")

    print("--- 2. Procesador de Texto (Modularidad) ---")
    p = ProcesadorTexto()
    p.procesar("¡Hola, Mundo! Hola de nuevo.")
    print(f"Estadísticas: {p.obtener_resumen()}\n")

    print("--- 3. Herencia (Métodos Protegidos) ---")
    try:
        c = Circulo(-5)
    except ValueError as e:
        print(f"Validación heredada funcionando: {e}\n")

    print("--- 4. Formulario (Validación Modular) ---")
    f = Formulario()
    datos_malos = {'email': 'no-es-email', 'pass': '123'}
    if not f.validar(datos_malos):
        print(f"Errores encontrados: {f.errores}")