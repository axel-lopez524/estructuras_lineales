from estructuras.lineales.nodo import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        # Crear un nuevo nodo
        new_node = Node(data)

        # Verificar si la lista está vacía
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        # Crear un nuevo nodo
        new_node = Node(data)

        # Verificar si la lista está vacía
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_at_beginning(self):
        # Verificar si la lista está vacía
        if self.head is None:
            return False

        # Si solo hay un nodo
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        return True

    def delete_at_end(self):
        # Verificar si la lista está vacía
        if self.head is None:
            return False

        # Si solo hay un nodo
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return True

        # Recorrer hasta el penúltimo nodo
        current = self.head

        while current.next != self.tail:
            current = current.next

        current.next = None
        self.tail = current

        return True

    def search(self, data):
        current_node = self.head

        while current_node is not None:
            if current_node.data == data:
                return True

            current_node = current_node.next

        return False

    def print_linked_list(self):
        temp = self.head

        print("Head -> ", end="")

        while temp is not None:
            print(temp.data, "->", end=" ")
            temp = temp.next

        print("<- Tail")
        
    def get_list(self):
        if self.head is None:
            return "La lista está vacía"

        temp = self.head
        resultado = "Head -> "

        while temp is not None:
            resultado += f"{temp.data} -> "
            temp = temp.next

        resultado += "<- Tail"

        return resultado

   