
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import Slot
import sys


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle("Botón presionar y soltar")
        self.setGeometry(100, 100, 400, 200)

        # Crear el botón
        self.boton = QPushButton("Pulsar", self)

        # El botón no será conmutable
        self.boton.setCheckable(False)

        self.setCentralWidget(self.boton)

        # Conectar las señales
        self.boton.pressed.connect(self.boton_presionado)
        self.boton.released.connect(self.boton_liberado)

    @Slot()
    def boton_presionado(self):
        self.boton.setText("Soltar")
        print("Botón presionado")

    @Slot()
    def boton_liberado(self):
        self.boton.setText("Pulsar")
        print("Botón liberado")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())