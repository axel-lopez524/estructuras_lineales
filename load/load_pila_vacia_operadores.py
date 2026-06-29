import sys
from PyQt5.QtWidgets import QDialog, QMessageBox, QApplication
from PyQt5.uic import loadUi

# 1. Importamos la lógica del convertidor que creamos
from estructuras.lineales.pila_vacia_para_operadores import ConvertidorInfijoPosfijo
class VentanaConvertidor(QDialog):
    def __init__(self):
        super().__init__()
        # 2. Carga tu archivo .ui diseñado en Qt Designer
        # (Si tu archivo .ui se llama diferente, ej: 'posfija.ui', cámbialo aquí)
        # Cambia "ui/inflija.ui" por "ui/posfija.ui"
        loadUi("ui/posfija.ui", self)  
        
        # 3. Conectar el botón para realizar la conversión
        # REVISIÓN: Cambia 'btn_convertir' por el objectName exacto de tu botón en Qt Designer
        self.btn_convertir.clicked.connect(self.procesar_conversion)

    def procesar_conversion(self):
        # 4. Leer la expresión ingresada por el usuario
        # REVISIÓN: Cambia 'txt_infija' por el objectName de tu Input/LineEdit
        expresion_inflija = self.txt_inflija.text().strip()
        
        if not expresion_inflija:
            QMessageBox.warning(self, "Error", "Por favor, ingrese una expresión infija válida.")
            return
            
        # 5. Ejecutar el algoritmo usando tu LinkedStack interna
        convertidor = ConvertidorInfijoPosfijo()
        resultado_posfijo = convertidor.convertir_a_posfija(expresion_inflija)
        
        # 6. Mostrar el resultado en la interfaz
        # REVISIÓN: Cambia 'lbl_resultado' por el objectName de tu Label o LineEdit de salida
        self.lbl_resultado.setText(resultado_posfijo)

# Bloque de prueba para ejecutar esta ventana de manera independiente
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaConvertidor()
    ventana.show()
    sys.exit(app.exec_())