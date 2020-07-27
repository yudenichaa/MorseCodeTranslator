from PyQt5 import QtWidgets, QtCore
from MorseTranslator import MorseTranslator


class TranslatorWidget(QtWidgets.QWidget):

    def _btn_load_from_file_clicked(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self,
                                                     "Select file to upload",
                                                     QtCore.QDir.homePath(),
                                                     "Text file (*.txt)")
        file_name = file[0]
        if not file_name:
            return

        source_file = QtCore.QFile(file_name)
        if not source_file.open(QtCore.QIODevice.ReadOnly):
            QtWidgets.QMessageBox.critical(self, self.windowTitle(),
                                           "Could not open file for reading" +
                                           file_name)
            return

        self._txt_source_text.setPlainText(source_file.readAll().data().decode("utf-8"))
        source_file.close()

    def _btn_translate_clicked(self):
        source_text = self._txt_source_text.toPlainText()
        if not source_text:
            QtWidgets.QMessageBox.information(self, self.windowTitle(),
                                              "Enter text to translate")
            return

        if self._cmb_translation_type.currentIndex() == 0:
            self._txt_result_text.setPlainText(MorseTranslator.translate_to_morse(source_text))
        else:
            self._txt_result_text.setPlainText(MorseTranslator.translate_from_morse(source_text))

    def _btn_save_to_file_clicked(self):
        result_text = self._txt_result_text.toPlainText()
        if not result_text:
            QtWidgets.QMessageBox.information(self, self.windowTitle(),
                                              "No data to save. "
                                              "Complete the translation.")
            return

        file = QtWidgets.QFileDialog.getOpenFileName(self,
                                                     "Select file to save",
                                                     QtCore.QDir.homePath(),
                                                     "Text file (*.txt)")
        file_name = file[0]
        if not file_name:
            return

        result_file = QtCore.QFile(file_name)
        if not result_file.open(QtCore.QIODevice.WriteOnly):
            QtWidgets.QMessageBox(self, self.windowTitle(),
                                  "Could not open file for writing " +
                                  file_name)
            return

        result_file.write(result_text.encode("utf-8"))
        result_file.close()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Morse code translator")

        lbl_source_text = QtWidgets.QLabel("Source text:")
        lbl_result_text = QtWidgets.QLabel("Translation result:")
        lbl_translation_type = QtWidgets.QLabel("Translate")

        btn_load_from_file = QtWidgets.QPushButton("Load from file")
        btn_translate = QtWidgets.QPushButton("Translate")
        btn_save_to_file = QtWidgets.QPushButton("Save to file")

        btn_load_from_file.clicked.connect(self._btn_load_from_file_clicked)
        btn_translate.clicked.connect(self._btn_translate_clicked)
        btn_save_to_file.clicked.connect(self._btn_save_to_file_clicked)

        self._txt_source_text = QtWidgets.QTextEdit()
        self._txt_source_text.setFontPointSize(14)

        self._txt_result_text = QtWidgets.QTextEdit()
        self._txt_result_text.setFontPointSize(14)

        self._cmb_translation_type = QtWidgets.QComboBox()
        self._cmb_translation_type.addItems(("to Morse", "from Morse"))
        self._cmb_translation_type.setCurrentIndex(0)

        layout_for_source_text_header = QtWidgets.QHBoxLayout()
        layout_for_source_text_header.setAlignment(QtCore.Qt.AlignLeft)
        layout_for_source_text_header.addWidget(lbl_source_text)
        layout_for_source_text_header.addWidget(btn_load_from_file)
        layout_for_source_text_header.addWidget(lbl_translation_type)
        layout_for_source_text_header.addWidget(self._cmb_translation_type)
        layout_for_source_text_header.addWidget(btn_translate)

        layout_for_source_text_column = QtWidgets.QVBoxLayout()
        layout_for_source_text_column.addLayout(layout_for_source_text_header)
        layout_for_source_text_column.addWidget(self._txt_source_text)

        layout_for_result_text_header = QtWidgets.QHBoxLayout()
        layout_for_result_text_header.setAlignment(QtCore.Qt.AlignLeft)
        layout_for_result_text_header.addWidget(lbl_result_text)
        layout_for_result_text_header.addWidget(btn_save_to_file)

        layout_for_result_text_column = QtWidgets.QVBoxLayout()
        layout_for_result_text_column.addLayout(layout_for_result_text_header)
        layout_for_result_text_column.addWidget(self._txt_result_text)

        layout_for_translation_widget = QtWidgets.QHBoxLayout()
        layout_for_translation_widget.addLayout(layout_for_source_text_column)
        layout_for_translation_widget.addLayout(layout_for_result_text_column)

        self.setLayout(layout_for_translation_widget)
