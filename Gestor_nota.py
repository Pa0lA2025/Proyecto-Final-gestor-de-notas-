cursos = []
historial = []
cola_revision = []

def agregar_curso(nombre, nota):
    if not nombre.strip():
        print("El nombre no puede estar vacío.")
        return
    if nota < 0 or nota > 100:
        print("La nota debe estar entre 0 y 100.")
        return
    cursos.append({"nombre": nombre, "nota": nota})
    print(f"Curso '{nombre}' agregado con nota {nota}.")

def listar_cursos():
    if cursos:
        print("\nCursos registrados:")
        for i, curso in enumerate(cursos, start=1):
            print(f"{i}. {curso['nombre']} - Nota: {curso['nota']}")
    else:
        print("No hay cursos registrados.")

def promedio_notas_cursos():
    if cursos:
        promedio = sum(c["nota"] for c in cursos) / len(cursos)
        print(f"Promedio general: {promedio:.2f}")
    else:
        print("No hay cursos registrados.")

def contar_aprobados_reprobados():
    aprobados = sum(1 for c in cursos if c["nota"] >= 60)
    reprobados = len(cursos) - aprobados
    print(f"Cursos aprobados: {aprobados}")
    print(f"Cursos reprobados: {reprobados}")

def buscar_lineal():
    nombre = input("Ingrese el nombre del curso: ").lower()
    encontrados = [c for c in cursos if nombre in c["nombre"].lower()]
    if encontrados:
        for curso in encontrados:
            print(f"Curso encontrado: {curso['nombre']} - Nota: {curso['nota']}")
    else:
        print("Curso no encontrado.")

def actualizar_nota():
    nombre = input("Ingrese el nombre del curso: ").lower()
    for curso in cursos:
        if curso["nombre"].lower() == nombre:
            nueva_nota = float(input("Ingrese la nueva nota: "))
            if nueva_nota < 0 or nueva_nota > 100:
                print("La nota debe estar entre 0 y 100.")
                return
            historial.append(f"Se actualizó: {curso['nombre']} - Nota anterior: {curso['nota']} → Nueva nota: {nueva_nota}")
            curso["nota"] = nueva_nota
            print("Nota actualizada correctamente.")
            return
    print("Curso no encontrado.")

def eliminar_curso():
    nombre = input("Ingrese el curso a eliminar: ").lower()
    for curso in cursos:
        if curso["nombre"].lower() == nombre:
            confirmacion = input("¿Está seguro que desea eliminarlo? (s/n): ").lower()
            if confirmacion == "s":
                historial.append(f"Se eliminó: {curso['nombre']} - Nota: {curso['nota']}")
                cursos.remove(curso)
                print("Curso eliminado correctamente.")
            else:
                print("Eliminación cancelada.")
            return
    print("Curso no encontrado.")

def ordenar_por_nota():
    n = len(cursos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if cursos[j]["nota"] < cursos[j + 1]["nota"]:
                cursos[j], cursos[j + 1] = cursos[j + 1], cursos[j]
    print("Cursos ordenados por nota:")
    listar_cursos()

def ordenar_por_nombre():
    for i in range(1, len(cursos)):
        clave = cursos[i]
        j = i - 1
        while j >= 0 and clave["nombre"].lower() < cursos[j]["nombre"].lower():
            cursos[j + 1] = cursos[j]
            j -= 1
        cursos[j + 1] = clave
    print("Cursos ordenados por nombre:")
    listar_cursos()

def buscar_binaria():
    ordenar_por_nombre()
    nombre = input("Ingrese el nombre del curso a buscar: ").lower()
    izquierda, derecha = 0, len(cursos) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        actual = cursos[medio]["nombre"].lower()
        if actual == nombre:
            print(f"Curso encontrado: {cursos[medio]['nombre']} - Nota: {cursos[medio]['nota']}")
            return
        elif actual < nombre:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    print("Curso no encontrado.")

def simular_cola_revision():
    print("Ingrese curso para revisión (escriba 'fin' para terminar):")
    while True:
        nombre = input("> ").strip()
        if nombre.lower() == "fin":
            break
        cola_revision.append(nombre)
    print("Procesando solicitudes:")
    while cola_revision:
        curso = cola_revision.pop(0)
        print(f"Revisando: {curso}")

def mostrar_historial():
    if not historial:
        print("No hay cambios registrados.")
    else:
        print("Historial de cambios recientes:")
        for i, cambio in enumerate(reversed(historial), start=1):
            print(f"{i}. {cambio}")

# -------------------------------
# Menú Principal
# -------------------------------
def menu():
    while True:
        print("\n====== GESTOR DE NOTAS ACADÉMICAS ======")
        print("1. Registrar nuevo curso")
        print("2. Mostrar todos los cursos y notas")
        print("3. Calcular promedio general")
        print("4. Contar cursos aprobados y reprobados")
        print("5. Buscar curso por nombre (búsqueda lineal)")
        print("6. Actualizar nota de un curso")
        print("7. Eliminar un curso")
        print("8. Ordenar cursos por nota (ordenamiento burbuja)")
        print("9. Ordenar cursos por nombre (ordenamiento inserción)")
        print("10. Buscar curso por nombre (búsqueda binaria)")
        print("11. Simular cola de solicitudes de revisión")
        print("12. Mostrar historial de cambios (pila)")
        print("13. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del curso: ")
            nota = float(input("Nota: "))
            agregar_curso(nombre, nota)
        elif opcion == "2":
            listar_cursos()
        elif opcion == "3":
            promedio_notas_cursos()
        elif opcion == "4":
            contar_aprobados_reprobados()
        elif opcion == "5":
            buscar_lineal()
        elif opcion == "6":
            actualizar_nota()
        elif opcion == "7":
            eliminar_curso()
        elif opcion == "8":
            ordenar_por_nota()
        elif opcion == "9":
            ordenar_por_nombre()
        elif opcion == "10":
            buscar_binaria()
        elif opcion == "11":
            simular_cola_revision()
        elif opcion == "12":
            mostrar_historial()
        elif opcion == "13":
            print("Gracias por usar el Gestor de Notas Académicas. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# -------------------------------
# Ejecutar el programa
# -------------------------------
if __name__ == "__main__":
    menu()
