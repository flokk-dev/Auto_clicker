# SYSTEME IMPORT
import time
import random
import threading

# EXTERN LIBRARY IMPORT
import pyautogui


# CLASS TO CONFIGURE THE AUTO CLICK
class AutoClicker(threading.Thread):
    def __init__(self):
        super(AutoClicker, self).__init__()

        self._delay = 0.40

        self._item_pos = (1599, 314)
        self._vendre_pos = (1050, 997)
        self._valider_pos = (917, 789)

        self._running = False
        self._program_run = True

        self._adv = {
            0: (2286, 623),
            1: (2551, 623),
            2: (2838, 623)
        }

    def startAC(self):
        if not self._running:
            self._running = True

    def stopAC(self):
        self._running = False

    def exitAC(self):
        self._running = False
        self._program_run = False

    def run(self):
        while self._program_run:
            while self._running:
                # ITEM
                pyautogui.click(x=1162, y=695)
                time.sleep(2)
                pyautogui.click(x=1162, y=695)
                time.sleep(30)

                """
                pyautogui.click(x=2427, y=895)
                time.sleep(2)
                # time.sleep(random.randint(2, 5))

                pyautogui.click(x=2427, y=895)
                time.sleep(2)
                # time.sleep(random.randint(2, 5))

                # VENDRE
                # adv_pos = self._adv[random.randint(0, 2)]
                pyautogui.click(x=2838, y=623)
                time.sleep(2)
                # time.sleep(random.randint(2, 5))

                # CLICK
                pyautogui.click(x=1788, y=68)
                time.sleep(3)
                # time.sleep(random.randint(3, 5))
                """
