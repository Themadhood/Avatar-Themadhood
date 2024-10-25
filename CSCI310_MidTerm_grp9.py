import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication
from PySide6.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
import time

class DroneController(QObject):
    # Signal to update the GUI
    brainwaveDetected = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.brainwave_data = None  # Placeholder for actual brainwave data
        self.current_action = None

    @pyqtSlot(str)
    def processCommand(self, command):
        """ Manually execute a command from the GUI. """
        print(f"Manual command received: {command}")
        self.executeCommand(command)

    def executeCommand(self, command):
        """ Send the command to the drone. """
        # Here we simulate the command being executed
        print(f"Executing command: {command}")
        # In real-life, integrate with your drone SDK to send the signal

    def processBrainwave(self):
        """ Example method that gets triggered automatically via brainwave signals. """
        # Simulate brainwave signal fetching
        brainwave_result = self.getBrainwaveSignal()

        if brainwave_result:
            print(f"Brainwave signal detected: {brainwave_result}")
            self.executeCommand(brainwave_result)
            # Emit signal to update the GUI
            self.brainwaveDetected.emit(brainwave_result)

    def getBrainwaveSignal(self):
        """ Simulate reading from brainwave device (in reality, fetch from SDK) """
        # Randomly returning a command for demonstration purposes
        brainwave_signals = ['takeoff', 'right', 'left', 'forward', 'backward', 'land']
        self.current_action = brainwave_signals[int(time.time()) % len(brainwave_signals)]
        return self.current_action

def main():
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Create controller object
    droneController = DroneController()

    # Expose backend to QML
    engine.rootContext().setContextProperty(backend,droneController)

    # Load the QML file
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(qml_file)

    if not engine.rootObjects():
        sys.exit(-1)

    # Start the app's event loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
