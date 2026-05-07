import datetime

# --- ESTRUCTURA DE DATOS INICIAL ---
# El diccionario 'inventario' utiliza nombres de equipos como llaves.
# Cada valor es otro diccionario con el estado y la lista de préstamos.
inventario = {
    "Laptop-01": {"disponible": True, "prestamos": []},
    "Tablet-05": {"disponible": True, "prestamos": []}
}

def mostrar_equipos():
    """Muestra todos los equipos y su estado actual."""
    print("\n--- ESTADO DEL INVENTARIO ---")
    if not inventario:
        print("No hay equipos registrados en el sistema.")
        return

    for equipo, datos in inventario.items():
        estado = "Disponible" if datos["disponible"] else "PRESTADO"
        print(f"Equipo: {equipo:15} | Estado: {estado}")

def registrar_prestamo():
    """Registra un nuevo préstamo usando tuplas (usuario, fecha)."""
    mostrar_equipos()
    nombre_equipo = input("\nIngrese el nombre exacto del equipo a prestar: ")

    if nombre_equipo in inventario:
        if inventario[nombre_equipo]["disponible"]:
            usuario = input("Nombre del usuario: ")
            # Usamos la fecha actual del sistema
            fecha = datetime.date.today().strftime("%d/%m/%Y")
            
            # CREACIÓN DE LA TUPLA (Inmutable para integridad de datos)
            registro = (usuario, fecha)
            
            # Actualización del inventario
            inventario[nombre_equipo]["prestamos"].append(registro)
            inventario[nombre_equipo]["disponible"] = False
            
            print(f"\n✅ Préstamo registrado: {nombre_equipo} entregado a {usuario}.")
        else:
            print("\n❌ Error: El equipo ya se encuentra prestado.")
    else:
        print("\n❌ Error: El equipo no existe en el sistema.")

def devolver_equipo():
    """Marca un equipo como disponible nuevamente."""
    nombre_equipo = input("\nIngrese el nombre del equipo a devolver: ")

    if nombre_equipo in inventario:
        if not inventario[nombre_equipo]["disponible"]:
            inventario[nombre_equipo]["disponible"] = True
            print(f"\n✅ Devolución exitosa: {nombre_equipo} ahora está disponible.")
        else:
            print("\n⚠️ El equipo ya estaba en la biblioteca (disponible).")
    else:
        print("\n❌ Error: El equipo no existe.")

def ver_historial():
    """Recorre el historial almacenado en listas de tuplas."""
    print("\n--- HISTORIAL COMPLETO DE PRÉSTAMOS ---")
    for equipo, datos in inventario.items():
        print(f"\nEquipo: {equipo}")
        if datos["prestamos"]:
            # Recorremos la lista de tuplas
            for i, (usuario, fecha) in enumerate(datos["prestamos"], 1):
                print(f"  {i}. Usuario: {usuario:15} | Fecha: {fecha}")
        else:
            print("  (Sin préstamos registrados)")

def agregar_equipo():
    """Añade un nuevo equipo al diccionario principal."""
    nombre = input("\nNombre del nuevo equipo: ")
    if nombre not in inventario:
        inventario[nombre] = {"disponible": True, "prestamos": []}
        print(f"\n✅ Equipo '{nombre}' agregado exitosamente.")
    else:
        print("\n❌ Error: El equipo ya existe.")

def menu():
    """Función principal que gestiona el flujo del programa."""
    while True:
        print("\n========================================")
        print("  SISTEMA DE PRÉSTAMOS DE EQUIPOS")
        print("========================================")
        print("1. Ver equipos disponibles")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial de préstamos")
        print("5. Agregar nuevo equipo")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            mostrar_equipos()
        elif opcion == "2":
            registrar_prestamo()
        elif opcion == "3":
            devolver_equipo()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            agregar_equipo()
        elif opcion == "6":
            print("Saliendo del sistema... ¡Hasta pronto!")
            break
        else:
            print("\n❌ Opción no válida. Intente de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    menu()