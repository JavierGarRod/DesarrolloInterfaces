import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit


class EditorNotas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 350)

        self.editor = QTextEdit()
        self.editor.setPlaceholderText("Escribe aquí tus notas")
        self.editor.setAcceptRichText(False)  # solo texto plano
        self.editor.textChanged.connect(self.actualizar_titulo)
        self.setCentralWidget(self.editor)

        # Título inicial: «Editor de notas — 0 caracteres»
        self.actualizar_titulo()

    @Slot()
    def actualizar_titulo(self):
        # textChanged no envía el texto, hay que pedirlo al editor
        total = len(self.editor.toPlainText())
        palabra = "carácter" if total == 1 else "caracteres"
        self.setWindowTitle(f"Editor de notas — {total} {palabra}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = EditorNotas()
    ventana.show()
    sys.exit(app.exec())