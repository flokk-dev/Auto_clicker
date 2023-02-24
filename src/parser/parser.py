# SYSTEME IMPORT
import configparser

# PROJECT IMPORT
from paths import path


class parserCAC:
    def __init__(self):
        # initialise configParser
        self._configParser = configparser.ConfigParser()

        # initialise keys
        self._fonctionnality = dict()
        self._initialise()

    def _initialise(self):
        self._configParser.read(path.CONFIG_F)

        for f in self._configParser.sections():
            self._fonctionnality[f] = dict()
            for e in self._configParser[f]:
                self._fonctionnality[f][e] = self._configParser.get(f, e)

    def getKeyCode(self, fonctionnality):
        return self._fonctionnality.get(fonctionnality).get("keycode")

    def get_startKeyCode(self):
        return self.getKeyCode("start")

    def get_stopKeyCode(self):
        return self.getKeyCode("stop")

    def get_selectKeyCode(self):
        return self.getKeyCode("select")

    def get_pauseKeyCode(self):
        return self.getKeyCode("pause")

    def get_exitKeyCode(self):
        return self.getKeyCode("exit")

    def _setKeyCode(self, fonctionnality, keyCode):
        self._configParser.set(fonctionnality, "keycode", keyCode)

    def setKeysCode(self):
        self._configParser.read(path.CONFIG_F)

        print("\n")
        for f in self._fonctionnality:
            desc = self._fonctionnality.get(f).get("desc").replace("\"", "")
            print(f'Choose a key to {desc}:')
            self._setKeyCode(f, input()[0])
        print("\n")
        print("Settings finished, you can now use the autoClicker")

        with open(path.CONFIG_F, 'w') as f:
            self._configParser.write(f)

    def showFonctionnalies(self):
        self._configParser.read(path.CONFIG_F)

        print("\n")
        print("These are the autoclicker functionalities:")
        for f in self._fonctionnality.keys():
            desc = self._fonctionnality.get(f).get("desc").replace("\"", "")
            keyCode = self._fonctionnality.get(f).get("keycode")
            print(f"\t- {desc}: {keyCode}.")
