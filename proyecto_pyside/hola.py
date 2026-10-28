import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
etiqueta = QLabel("¡Hola, PySide6!")
etiqueta.resize(300, 100)
etiqueta.show()
sys.exit(app.exec())