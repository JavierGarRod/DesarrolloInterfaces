
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import Slot
import sys


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        # Estado inicial de la funcionalidad
        self.notificaciones_activadas = False

        # Configuración de la ventana
        self.setWindowTitle("Notificaciones desactivadas")
        self.setGeometry(100, 100, 400, 200)

        # Creación del botón conmutable
        self.boton = QPushButton("Activar notificaciones", self)
        self.boton.setCheckable(True)
        self.setCentralWidget(self.boton)

        # Conexión de señales y métodos receptores
        self.boton.clicked.connect(self.registrar_activacion)
        self.boton.toggled.connect(self.actualizar_estado)

    @Slot(bool)
    def registrar_activacion(self, estado):
        """Registra en consola las activaciones."""
        if estado:
            print("Notificaciones activadas.")
        else:
            print("Notificaciones desactivadas.")

    @Slot(bool)
    def actualizar_estado(self, estado):
        """Actualiza el título y el texto del botón."""
        self.notificaciones_activadas = estado

        if estado:
            self.setWindowTitle("Notificaciones activadas")
            self.boton.setText("Desactivar notificaciones")
        else:
            self.setWindowTitle("Notificaciones desactivadas")
            self.boton.setText("Activar notificaciones")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())