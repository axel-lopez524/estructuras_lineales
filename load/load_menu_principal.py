from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

from load.load_lista_enlazada_simple import MenuListaEnlazada


class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("ui/menu_principal.ui", self)

        self.actionLista_Enlazada.triggered.connect(
            self.abrir_lista_enlazada
        )

        self.action5_Salir.triggered.connect(self.close)

    def abrir_lista_enlazada(self):
        self.ventana_lista = MenuListaEnlazada()
        self.ventana_lista.show()