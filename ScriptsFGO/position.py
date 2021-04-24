import pyautogui, sys, time

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = '- X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        pix = pyautogui.pixel(x,y)
        tmp = str(pix)+str(positionStr)
        print(tmp)
        print('\b'*len(tmp), flush=True)
        time.sleep(1)
        if pyautogui.pixelMatchesColor(281, 237, (214, 100, 100),tolerance=10):
            print(tmp)
            print('\b'*len(tmp), flush=True)
            time.sleep(1)
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