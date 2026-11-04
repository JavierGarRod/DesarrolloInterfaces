import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class VentanaAlternativa(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuramos la ventana
        self.setWindowTitle("Instagram")
        self.resize(500, 300)
        self.setMinimumSize(350, 200)

        # Creamos un botón relacionado con la aplicación
        self.boton = QPushButton("Iniciar sesión")

        # Colocamos el botón en el centro
        self.setCentralWidget(self.boton)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Elegimos qué ventana queremos ejecutar
    ventana = VentanaAlternativa()
    # ventana = Ventana()

    ventana.show()

    # Iniciamos el bucle de eventos
    sys.exit(app.exec())