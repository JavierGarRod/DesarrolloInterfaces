import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow


class VentanaProyecto(QMainWindow):
    TITULO_VACIO = "Proyecto sin nombre"

    def __init__(self):
        super().__init__()
        self.resize(400, 80)

        self.campo = QLineEdit()
        self.campo.setPlaceholderText("Escribe el nombre del proyecto")
        self.campo.setMaxLength(30)
        self.campo.textChanged.connect(self.actualizar_titulo)
        self.setCentralWidget(self.campo)

        # Título inicial (el campo empieza vacío)
        self.actualizar_titulo(self.campo.text())

    @Slot(str)
    def actualizar_titulo(self, texto):
        nombre = texto.strip()
        if nombre:
            self.setWindowTitle(nombre.upper())
        else:
            self.setWindowTitle(self.TITULO_VACIO)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaProyecto()
    ventana.show()
    sys.exit(app.exec())