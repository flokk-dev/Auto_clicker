# IMPORT BIBLIOTHEQUES EXTERNES
from pynput.keyboard import Listener, KeyCode


class KeyboardListener:
    def __init__(self, configParser, autoClicker):
        self._configParser = configParser

        self._thread = autoClicker
        self._listener = None
        self._isListening = False

    def listen(self):
        self._listener = Listener(on_release=self.getPressedKeyCode)
        self._listener.start()

        self._isListening = True

    # BASE ALGORITHM
    def getPressedKeyCode(self, key):
        if self._isListening:
            if key == KeyCode(char=self._configParser.get_startKeyCode()):
                self._thread.startAC()
            elif key == KeyCode(char=self._configParser.get_stopKeyCode()):
                self._thread.stopAC()
            elif key == KeyCode(char=self._configParser.get_pauseKeyCode()):
                self._thread.stopAC()
                self._isListening = False

        if key == KeyCode(char=self._configParser.get_pauseKeyCode()):
            self._isListening = True
        elif key == KeyCode(char=self._configParser.get_exitKeyCode()):
            self._thread.exitAC()
            self._listener.stop()
