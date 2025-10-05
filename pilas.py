class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.items = []
        self.tope = 0  

    def esta_vacia(self):
        return self.tope == 0

    def esta_llena(self):
        return self.tope == self.capacidad

    def insertar(self, elemento):
        if self.esta_llena():
            print(" Error: Desbordamiento. La pila está llena.\n")
        else:
            self.items.append(elemento)
            self.tope += 1
            print(f" Se insertó '{elemento}' correctamente.")
            self.mostrar_estado()

    def eliminar(self):
        if self.esta_vacia():
            print(" Error: Subdesbordamiento. La pila está vacía.\n")
        else:
            eliminado = self.items.pop()
            self.tope -= 1
            print(f" Se eliminó '{eliminado}' correctamente.")
            self.mostrar_estado()

    def mostrar_estado(self):
        print(" Estado actual de la pila:")
        for i in range(self.tope - 1, -1, -1):
            print(f"| {self.items[i]} |")
        print("-----")
        print(f"TOPE = {self.tope}\n")

def menu():
    pila = Pila(8)  
    opcion = 0

    while opcion != 4:
        print("====== MENÚ DE PILA ======")
        print("1. Insertar elemento")
        print("2. Eliminar elemento")
        print("3. Mostrar pila")
        print("4. Salir")
        print("==========================")
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print(" Ingresa un número válido.\n")
            continue

        if opcion == 1:
            elemento = input("Ingresa el elemento a insertar: ")
            pila.insertar(elemento)
        elif opcion == 2:
            pila.eliminar()
        elif opcion == 3:
            pila.mostrar_estado()
        elif opcion == 4:
            print(" Saliendo del programa...")
        else:
            print(" Opción no válida. Intenta de nuevo.\n")

    print(f"\nPila final: {pila.items}")
    print(f"Total de elementos: {len(pila.items)}")

if __name__ == "__main__":
    menu()