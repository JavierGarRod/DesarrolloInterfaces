import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QComboBox, QMainWindow

# (texto visible, identificador corto)
TECNOLOGIAS = [
    ("Python", "py"),
    ("Java", "java"),
    ("JavaScript", "js"),
    ("C++", "cpp"),
    ("Rust", "rs"),
    ("Go", "go"),
]


class VentanaTecnologia(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 80)

        self.combo = QComboBox()
        for nombre, identificador in TECNOLOGIAS:
            # El segundo argumento es el dato interno asociado a la opción
            self.combo.addItem(nombre, identificador)
        self.combo.currentIndexChanged.connect(self.tecnologia_cambiada)
        self.setCentralWidget(self.combo)

        # Muestra la tecnología seleccionada al arrancar
        self.tecnologia_cambiada(self.combo.currentIndex())

    @Slot(int)
    def tecnologia_cambiada(self, indice):
        nombre = self.combo.itemText(indice)
        identificador = self.combo.itemData(indice)
        self.setWindowTitle(f"Tecnología: {nombre}")
        print(f"Índice: {indice} | Identificador: {identificador}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaTecnologia()
    ventana.show()
    sys.exit(app.exec())