# This Python file uses the following encoding: utf-8
import sys
import os

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

from Users import Users
from Model import Model
from Webcam import Webcam


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    #Object instances - Mitsuo
    engine = QQmlApplicationEngine()
    Users = Users()
    webcam = Webcam()
    model = Model()

    model.load_model()

    engine.rootContext().setContextProperty("user", Users)
    engine.rootContext().setContextProperty("webcam",webcam)

    engine.load(os.path.join(os.path.dirname(__file__), "main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())

