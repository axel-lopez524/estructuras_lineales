class NodoPila:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class PilaConvertidor:
    """Una pila interna garantizada para que el convertidor no marque error de métodos"""
    def __init__(self):
        self.superior = None

    def push(self, dato):
        nuevo_nodo = NodoPila(dato)
        nuevo_nodo.siguiente = self.superior
        self.superior = nuevo_nodo

    def pop(self):
        if self.is_empty():
            return None
        elemento = self.superior.dato
        self.superior = self.superior.siguiente
        return elemento

    def peek(self):
        if self.is_empty():
            return None
        return self.superior.dato

    def is_empty(self):
        return self.superior is None


class ConvertidorInfijoPosfijo:
    def obtener_precedencia(self, operador):
        if operador in ('+', '-'):
            return 1
        if operador in ('*', '/'):
            return 2
        if operador == '^':
            return 3
        return 0

    def convertir_a_posfija(self, expresion_infija):
        # Usamos nuestra pila interna garantizada con push y pop
        pila_operadores = PilaConvertidor()
        cadena_posfija = []

        # Separar elementos por caracteres
        elementos = expresion_infija.split() if ' ' in expresion_infija else list(expresion_infija)

        for elemento in elementos:
            if elemento.isalnum():
                cadena_posfija.append(elemento)
                
            elif elemento == '(':
                pila_operadores.push(elemento)
                
            elif elemento == ')':
                while not pila_operadores.is_empty() and pila_operadores.peek() != '(':
                    cadena_posfija.append(pila_operadores.pop())
                if not pila_operadores.is_empty() and pila_operadores.peek() == '(':
                    pila_operadores.pop()
                    
            # Si es un operador (+, -, *, /)
            else:
                while not pila_operadores.is_empty() and pila_operadores.peek() != '(' and \
                      self.obtener_precedencia(pila_operadores.peek()) >= self.obtener_precedencia(elemento):
                    cadena_posfija.append(pila_operadores.pop())
                pila_operadores.push(elemento)

        # Vaciar los operadores restantes
        while not pila_operadores.is_empty():
            cadena_posfija.append(pila_operadores.pop())

        return "".join(cadena_posfija)