from estructuras.lineales.nodo import Node

class LinkedStack:
    def __init__(self):
        self.top= None

        def push(self, dato):
            #insertar unn nuevo elemento en la pila""
            new_node = Node(dato)
            if self.is_empty():
                self.top = new_node
            else:
                new_node.next = self.top
                self.top = new_node

    # ... Tu método push se queda igual ...

    def pop(self):
        if self.is_empty():
            return None  # En lugar de falso, regresamos None si está vacía
        
        # Guardamos el dato del nodo que vamos a sacar antes de borrarlo
        operador_sacado = self.top.dato
        
        # Movemos el puntero al siguiente nodo
        self.top = self.top.next
        
        # ¡IMPORTANTE! Devolvemos el operador que extrajimos
        return operador_sacado

    def peek(self):
        if self.is_empty():
            return None
        return self.top.dato  # Asegúrate de regresar el dato del nodo superior

    def is_empty(self):
        return self.top is None


        elementos = []
        actual = self.top
        while actual:
            elementos.append(str(actual.data))
            actual = actual.next

        return " -> ".join(elementos)