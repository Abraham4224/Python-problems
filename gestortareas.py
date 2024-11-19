class Tarea:
    def __init__(self, descripcion, prioridad):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False

    def completar(self):
        self.completada = True

    def __str__(self):
        estado = "✔" if self.completada else "✘"
        return f"[{estado}] {self.descripcion} (Prioridad: {self.prioridad})"


class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        nueva_tarea = Tarea(descripcion, prioridad)
        self.tareas.append(nueva_tarea)

    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas por mostrar.")
            return
        for i, tarea in enumerate(self.tareas, start=1):
            print(f"{i}. {tarea}")

    def completar_tarea(self, indice):
        if 0 < indice <= len(self.tareas):
            self.tareas[indice - 1].completar()
            print("Tarea completada con éxito.")
        else:
            print("Índice no válido.")

    def eliminar_tarea(self, indice):
        if 0 < indice <= len(self.tareas):
            tarea_eliminada = self.tareas.pop(indice - 1)
            print(f"Tarea eliminada: {tarea_eliminada.descripcion}")
        else:
            print("Índice no válido.")


# Ejemplo de uso
def menu():
    gestor = GestorTareas()
    while True:
        print("\nGestor de Tareas")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            descripcion = input("Descripción de la tarea: ")
            prioridad = input("Prioridad (Alta, Media, Baja): ")
            gestor.agregar_tarea(descripcion, prioridad)
        elif opcion == "2":
            gestor.listar_tareas()
        elif opcion == "3":
            gestor.listar_tareas()
            indice = int(input("Índice de la tarea a completar: "))
            gestor.completar_tarea(indice)
        elif opcion == "4":
            gestor.listar_tareas()
            indice = int(input("Índice de la tarea a eliminar: "))
            gestor.eliminar_tarea(indice)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
