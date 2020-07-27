import sys
from PyQt5 import QtWidgets
from TranslatorWidget import TranslatorWidget


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
    translator_widget = TranslatorWidget()
    translator_widget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
