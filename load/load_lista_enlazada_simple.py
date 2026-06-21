from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from estructuras.lineales.lista_enlazada_simple import LinkedList


class MenuListaEnlazada(QDialog):
    def __init__(self):
        super().__init__()

        loadUi("ui/lista_enlazada.ui", self)

        self.lista_enlazada = LinkedList()

        
        self.btn_agregarInicio.clicked.connect(self.agregar_inicio)
        self.btn_agregarFinal.clicked.connect(self.agregar_final)
        self.btn_eliminarInicio.clicked.connect(self.eliminar_inicio)
        self.btn_eliminarFinal.clicked.connect(self.eliminar_final)
        self.btn_buscar.clicked.connect(self.buscar)

    def agregar_inicio(self):
        dato = self.txt_dato.text().strip()

        if dato == "":
            QMessageBox.warning(self, "Error", "Ingrese un dato")
            return

        self.lista_enlazada.insert_at_beginning(dato)
        self.txt_dato.clear()
        self.imprimir()

    def agregar_final(self):
        dato = self.txt_dato.text().strip()

        if dato == "":
            QMessageBox.warning(self, "Error", "Ingrese un dato")
            return

        self.lista_enlazada.insert_at_end(dato)
        self.txt_dato.clear()
        self.imprimir()

    def eliminar_inicio(self):
        if not self.lista_enlazada.delete_at_beginning():
            QMessageBox.warning(self, "Error", "La lista está vacía")

        self.imprimir()

    def eliminar_final(self):
        if not self.lista_enlazada.delete_at_end():
            QMessageBox.warning(self, "Error", "La lista está vacía")

        self.imprimir()

    def buscar(self):
        dato = self.txt_dato.text().strip()

        if dato == "":
            QMessageBox.warning(self, "Error", "Ingrese un dato para buscar")
            return

        if self.lista_enlazada.search(dato):
            QMessageBox.information(
                self,
                "Buscar",
                f"'{dato}' fue encontrado."
            )
        else:
            QMessageBox.warning(
                self,
                "Buscar",
                f"'{dato}' no fue encontrado."
            )

    def imprimir(self):
        self.lbl_resultado.setText(
            self.lista_enlazada.get_list()
        )