import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class VentanaBienvenida(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bienvenido a MiGestor de Tareas")
        self.resize(450, 250)

        etiqueta = QLabel(
            "¡Bienvenido a MiGestor de Tareas! "
            "Organiza tu día, anota tus ideas y no olvides nada importante."
        )

        # Tamaño de fuente de 20 puntos
        fuente = etiqueta.font()
        fuente.setPointSize(20)
        etiqueta.setFont(fuente)

        # Texto centrado horizontal y verticalmente
        etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Prueba: para colocar el texto en la parte inferior, usa
        # etiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        # Permite que el texto se reparta en varias líneas
        etiqueta.setWordWrap(True)

        self.setCentralWidget(etiqueta)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaBienvenida()
    ventana.show()
    sys.exit(app.exec())