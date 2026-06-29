from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

from load.load_lista_enlazada_simple import MenuListaEnlazada
from load.load_pila_vacia_operadores import VentanaConvertidor

class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        
        uic.loadUi("ui/menu_principal.ui", self)
        
        # 1. Conexión de la Lista Enlazada (Usa el nombre correcto de tu submenú)
        self.actionLista_Enlazada.triggered.connect(self.abrir_lista_enlazada)
        
        # 2. 🟢 ¡AQUÍ ESTÁ LA CORRECCIÓN CLAVE! 
        # Usamos 'actioninflija' que es el objectName real de tu Qt Designer
        self.actioninflija.triggered.connect(self.abrir_convertidor)
        
        # 3. Conexión de Salir
        self.action5_Salir.triggered.connect(self.close)

    def abrir_lista_enlazada(self):
        self.ventana_lista = MenuListaEnlazada()
        self.ventana_lista.show()

    def abrir_convertidor(self):
        # Instancia y muestra de forma limpia tu convertidor
        self.ventana_convertidor = VentanaConvertidor()
        self.ventana_convertidor.exec_()