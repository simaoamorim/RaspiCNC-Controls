#!/usr/bin/env python3
from PySide2.QtCore import Slot, QProcess, QDir
from PySide2.QtWidgets import QApplication, QWidget, QMessageBox

from ui.mainwindow import Ui_MainWindow

global mainwindow
global process


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


@Slot()
def finished():
    global process, mainwindow
    mainwindow.setEnabled(True)
    if process.exitCode() != 0:
        m = QMessageBox(
            QMessageBox.Critical,
            "Error",
            str(process.readAll(), "utf-8")
        )
        m.exec_()
        m.deleteLater()
    process.deleteLater()


@Slot()
def errored(error: QProcess.ProcessError):
    mainwindow.setEnabled(True)
    m = QMessageBox(
        QMessageBox.Critical,
        "Error",
        error.__str__()
    )
    m.exec_()
    m.deleteLater()
    process.deleteLater()


def prepare_process(
        program: str,
        args: [str],
        working_directory: str
        ):
    global process, mainwindow
    process = QProcess(app)
    process.error.connect(errored)
    process.setProgram(program)
    process.setArguments(args)
    process.setWorkingDirectory(working_directory)
    process.finished.connect(finished)



@Slot()
def startprogramloader():
    global process, mainwindow
    qdir = QDir()
    qdir.cd("./modules/SerialProgramLoader/src")
    prepare_process("python3", ["main.py"], qdir.path())
    mainwindow.setDisabled(True)
    process.start()


@Slot()
def startremotecontrol():
    global process, mainwindow
    qdir = QDir()
    # qdir.cd("./modules/xhc_receiver/src")
    prepare_process("bash", ["start_xhc.sh"], qdir.path())
    mainwindow.setDisabled(True)
    process.start()


if __name__ == '__main__':
    app = QApplication()

    mainwindow = MainWindow()
    mainwindow.ui.programLoaderButton.clicked.connect(startprogramloader)
    mainwindow.ui.remoteControlButton.clicked.connect(startremotecontrol)
    mainwindow.showMaximized()

    exit(app.exec_())
