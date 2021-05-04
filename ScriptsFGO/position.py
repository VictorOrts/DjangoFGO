import pyautogui, sys, time
import os
SHORT_TIME_WAIT  = 3
MEDIUM_TIME_WAIT = 6
def mouse_cycle(x,y):
    pyautogui.PAUSE = SHORT_TIME_WAIT
    pyautogui.moveTo(x, y)
    pyautogui.PAUSE = SHORT_TIME_WAIT
    pyautogui.click(button='left')
    pyautogui.PAUSE = MEDIUM_TIME_WAIT
try:
    #while True:
    pyautogui.PAUSE = 2 
    for listPos in pyautogui.locateAllOnScreen('img/atk_up.png',confidence=0.6):
        pyautogui.PAUSE = 2
        calculatemidx =listPos.left +(listPos.width*0.5)
        calculatemidy =listPos.top +(listPos.width*0.5)
        mouse_cycle(calculatemidx,calculatemidy)
        #else:
    
            #print("No coincide")
except KeyboardInterrupt:
    print('\n')
"""
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
"""
