# Proyecto: Clases, Objetos y Encapsulación en Python

## Descripción General

Este proyecto reúne diferentes ejemplos prácticos sobre Programación Orientada a Objetos (POO) en Python. A través de varios ejercicios y talleres se trabajan conceptos fundamentales como:

* Clases y objetos.
* Constructores.
* Métodos.
* Atributos.
* Encapsulación.
* Propiedades.
* Getters y Setters.
* Métodos privados.
* Validaciones.

El objetivo principal del proyecto es comprender cómo se diseñan clases en Python y cómo aplicar buenas prácticas de encapsulación para proteger y organizar la información dentro de los objetos.

---
# Explicación del Diseño de Clases y Encapsulación

## 1. Diseño de Clases

Las clases fueron diseñadas para representar objetos del mundo real, permitiendo almacenar información y ejecutar acciones relacionadas con cada objeto.

### Ejemplo: Clase `Estudiante`

```python
class Estudiante:
    universidad = "Universidad Autónoma"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

### Explicación

* `universidad` es un atributo de clase compartido por todos los estudiantes.
* `nombre` y `edad` son atributos de instancia.
* El constructor `__init__()` permite inicializar cada objeto con datos personalizados.

Este diseño permite crear múltiples estudiantes independientes, cada uno con su propia información.

---

## 2. Constructores

Los constructores se utilizan para inicializar objetos automáticamente.

### Ejemplo

```python
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
```

### Características Implementadas

* Inicialización automática.
* Valores predeterminados.
* Validaciones.
* Cálculos automáticos.
* Constructores alternativos usando `@classmethod`.

Los constructores ayudan a mantener consistencia en los objetos desde el momento de su creación.

---

## 3. Métodos

Los métodos representan acciones que un objeto puede realizar.

### Ejemplo

```python
class CuentaBancaria:
    def depositar(self, cantidad):
        self._saldo += cantidad
```

### Explicación

Los métodos permiten:

* Modificar atributos.
* Validar información.
* Ejecutar lógica de negocio.
* Proteger el acceso a datos sensibles.

En el proyecto se implementaron métodos para:

* Depositar dinero.
* Retirar dinero.
* Encender y apagar vehículos.
* Calcular estadísticas.
* Gestionar préstamos.

---

# Encapsulación

La encapsulación es uno de los principios más importantes de la Programación Orientada a Objetos.

Consiste en proteger los datos internos de un objeto para evitar modificaciones incorrectas.

## Atributos Privados

### Ejemplo

```python
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial, pin):
        self.__pin = pin
```

### Explicación

* El atributo `__pin` es privado.
* No puede ser accedido directamente desde fuera de la clase.
* Python aplica *name mangling* para ocultarlo.

Esto mejora la seguridad y evita manipulaciones indebidas.

---

## Getters y Setters

Los getters y setters permiten controlar cómo se accede o modifica un atributo.

### Ejemplo

```python
@property
 def saldo(self):
     return self._saldo
```

### Beneficios

* Validación de datos.
* Mayor control.
* Protección de atributos.
* Evita inconsistencias.

---

## Propiedades

Las propiedades permiten usar métodos como si fueran atributos.

### Ejemplo

```python
@celsius.setter
 def celsius(self, valor):
     if valor < -273.15:
         raise ValueError("No puede ser menor que el cero absoluto")
```

### Explicación

Gracias a las propiedades:

* Se pueden validar datos automáticamente.
* El código es más limpio.
* Se evita que el usuario ingrese valores inválidos.

---

## Métodos Privados

Los métodos privados se utilizan para dividir lógica interna que no debe ser utilizada directamente.

### Ventajas

* Mayor organización.
* Código más limpio.
* Protección de procesos internos.
* Facilita mantenimiento.

---

# Talleres y Retos

## Taller Libro

El archivo `Taller_libro.py` implementa una clase `Libro` con:

* Constructor.
* Métodos.
* Validación.
* Gestión de disponibilidad.

### Funcionalidades

* Prestar libros.
* Devolver libros.
* Consultar información.

Este taller permitió aplicar todos los conceptos básicos de clases y objetos.

---

## Taller Encapsulación

El archivo `Taller.py` implementa una cuenta bancaria encapsulada.

### Características

* Atributos protegidos.
* Uso de propiedades.
* Validación de saldo.
* Restricción de modificación del titular.

Este ejercicio demuestra cómo proteger información crítica dentro de una clase.

---

## Reto: Sistema de Préstamos

El reto `prestamos_equipo.py` implementa un sistema completo de gestión de préstamos de equipos.

### Funcionalidades

* Registro de equipos.
* Registro de préstamos.
* Historial.
* Devoluciones.
* Manejo de inventario.

### Conceptos Aplicados

* Diccionarios.
* Tuplas.
* Funciones.
* Estructuras de control.
* Manejo de fechas.
* Organización modular.

---

# Ejemplos de Ejecución en Consola (Capturas de Terminal)

Todas las imágenes utilizadas en este README corresponden únicamente a salidas de ejecución en la terminal de Visual Studio Code. Las capturas muestran los resultados obtenidos al ejecutar los diferentes archivos Python relacionados con clases, objetos y encapsulación.

## Ejecución de Atributos en Terminal

### Salida en Consola

![Resultado Atributos](images/Clase_objeto/Atributo/Captura%20de%20pantalla%202026-05-06%20202421.png)

---

## Ejecución de Constructores en Terminal

### Salida en Consola

![Resultado Constructores](images/Clase_objeto/Constructor/Captura%20de%20pantalla%202026-05-06%20202604.png)

---

## Ejecución de Métodos en Terminal

### Salida en Consola

![Resultado Métodos](images/Clase_objeto/Metodo/Captura%20de%20pantalla%202026-05-06%20202723.png)

---

## Ejecución de Encapsulación en Terminal

### Salida en Consola

![Resultado Encapsulación](images/Encapsulacion/Atributos_Privados/Captura%20de%20pantalla%202026-05-06%20203024.png)

---

## Ejecución de Getters y Setters en Terminal

### Salida en Consola

![Resultado Getters y Setters](images/Encapsulacion/Getters_Setters/Captura%20de%20pantalla%202026-05-06%20203112.png)

---

## Ejecución de Métodos Privados en Terminal

### Salida en Consola

![Resultado Métodos Privados](images/Encapsulacion/Metodos_Privados/Captura%20de%20pantalla%202026-05-06%20203151.png)

---

# Cómo Ejecutar el Proyecto

## Requisitos

* Python 3 instalado.
* Visual Studio Code.
* Extensión Markdown Preview Enhanced.

---

## Ejecución

### Ejecutar un archivo

```bash
python nombre_archivo.py
```

### Ejemplo

```bash
python Atributos.py
```

---

# Tecnologías Utilizadas

* Python 3
* Visual Studio Code
* Markdown Preview Enhanced

---

# Reflexión Personal

Este proyecto me enseñó que la programación robusta se basa en dos pilares: orden y protección.

Gracias a la encapsulación, comprendí que proteger los datos internos de una clase mediante atributos privados y propiedades no es una restricción, sino una garantía de que el sistema no fallará por manipulaciones externas incorrectas.

Además, integrar estructuras como diccionarios y tuplas me permitió transformar un flujo de datos complejo en una herramienta organizada. Aprendí que la claridad visual en la interfaz es tan vital como la lógica del código; si la información no es legible, el sistema no es útil. En definitiva, este proceso me capacitó para escribir código más profesional, escalable y centrado en el usuario.

---

# Conclusión

El desarrollo de este sistema permitió integrar con éxito la lógica de negocio con una interfaz de usuario limpia. El uso de encapsulación y propiedades garantizó que los datos sensibles estuvieran protegidos, mientras que la combinación de diccionarios y tuplas ofreció una gestión de inventario eficiente e inmutable. En definitiva, el proyecto demuestra que un código profesional no solo debe ser funcional, sino también seguro, organizado y fácil de interpretar para el usuario final.