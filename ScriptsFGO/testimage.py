import pyautogui, sys, time

print('Press Ctrl-C to quit.')
try:
    time.sleep(3)
    pos = pyautogui.locateAllOnScreen('battle3x3.png')
    print(pos)
    checkbattle = pyautogui.locateOnScreen('battle3x3.png',grayscale=True)
    print(checkbattle)
    print(pyautogui.locateCenterOnScreen('battle3x3.png',grayscale=True))

except KeyboardInterrupt:
    print('\n')