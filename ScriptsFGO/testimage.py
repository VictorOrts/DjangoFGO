import pyautogui, sys, time

print('Press Ctrl-C to quit.')
try:
    time.sleep(3)
    checkbattle = pyautogui.locateOnScreen('ok.png',confidence=0.7)
    if pyautogui.locateOnScreen('ok.png',confidence=0.7):
        print(checkbattle)
    else:
        print("Es none")
    print(pyautogui.locateCenterOnScreen('ok.png',confidence=0.7))

except KeyboardInterrupt:
    print('\n')