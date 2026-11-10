import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow


class VentanaNotificaciones(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 80)

        self.casilla = QCheckBox("Activar notificaciones")
        self.casilla.setChecked(False)  # desmarcada al iniciar
        self.casilla.toggled.connect(self.cambiar_estado)
        self.setCentralWidget(self.casilla)

        self.setWindowTitle("Notificaciones desactivadas")

    @Slot(bool)
    def cambiar_estado(self, activada):
        if activada:
            self.setWindowTitle("Notificaciones activadas")
            print("Casilla marcada: notificaciones activadas")
        else:
            self.setWindowTitle("Notificaciones desactivadas")
            print("Casilla desmarcada: notificaciones desactivadas")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaNotificaciones()
    ventana.show()
    sys.exit(app.exec())