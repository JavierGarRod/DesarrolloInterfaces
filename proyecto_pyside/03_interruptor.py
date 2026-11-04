import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema apagado")
        self.resize(400, 180)

        # Creamos un botón conmutable
        self.boton = QPushButton("Encender")
        self.boton.setCheckable(True)

        # Conectamos las señales
        self.boton.clicked.connect(self.registrar_clic)
        self.boton.toggled.connect(self.actualizar_estado)

        self.boton.setChecked(True)

        self.setCentralWidget(self.boton)

    @Slot(bool)
    def registrar_clic(self, marcado):
        print(f"Clic recibido. Estado: {marcado}")

    @Slot(bool)
    def actualizar_estado(self, encendido):
        if encendido:
            self.setWindowTitle("Sistema encendido")
            self.boton.setText("Apagar")
        else:
            self.setWindowTitle("Sistema apagado")
            self.boton.setText("Encender")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())