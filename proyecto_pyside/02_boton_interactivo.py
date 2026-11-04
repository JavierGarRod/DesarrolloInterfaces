import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi primer botón interactivo")
        self.resize(400, 200)

        # Creamos el botón
        self.boton = QPushButton("Saludar")

        # Conectamos la señal con nuestro método
        self.boton.clicked.connect(self.saludar)

        self.setCentralWidget(self.boton)

    def saludar(self):
        print("¡Hola! Has pulsado el botón.")
        self.boton.setText("¡Saludo enviado!")
        self.setWindowTitle("¡Saludo realizado!")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())