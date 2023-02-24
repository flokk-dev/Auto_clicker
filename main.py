# PROJECT IMPORT
from src.parser.parserCAC import parserCAC
from src.keyboardListener.keyboardListener import KeyboardListener
from src.autoClicker.autoClicker import AutoClicker

# Settings of the parameters
parser = parserCAC()
parser.showFonctionnalies()

autoClicker = AutoClicker()
autoClicker.start()
autoClicker.startAC()

keyboardListener = KeyboardListener(parser, autoClicker)
keyboardListener.listen()
