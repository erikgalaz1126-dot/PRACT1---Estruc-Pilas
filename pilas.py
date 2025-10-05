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
            print(f" Error: Desbordamiento. No se puede insertar {elemento}. La pila está llena.")
        else:
            self.items.append(elemento)
            self.tope += 1
            print(f" Insertar({elemento}) → Pila: {self.items} | TOPE = {self.tope}")

    def eliminar(self, etiqueta):
        if self.esta_vacia():
            print(f" Error: Subdesbordamiento. No se puede eliminar ({etiqueta}). La pila está vacía.")
        else:
            elemento = self.items.pop()
            self.tope -= 1
            print(f" Eliminar({etiqueta}) → Se quitó {elemento} | Pila: {self.items} | TOPE = {self.tope}")

pila = Pila(8) 

print("=== ESTADO INICIAL ===")
print(f"Pila: {pila.items} | TOPE = {pila.tope}\n")

pila.insertar("X")   
pila.insertar("Y")   
pila.eliminar("Z")   
pila.eliminar("T")   
pila.eliminar("U")   
pila.insertar("V")   
pila.insertar("W")  
pila.eliminar("p")   
pila.insertar("R")   

print("\n=== ESTADO FINAL ===")
print(f"Pila final: {pila.items} | TOPE = {pila.tope}")
print(f"Total de elementos en la pila: {len(pila.items)}")
