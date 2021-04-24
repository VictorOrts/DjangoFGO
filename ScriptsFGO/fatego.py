import pyautogui, sys, time
repeat_game = 0

def skillUse():
    print("Usa skill")
    pyautogui.PAUSE = 6
    pyautogui.moveTo(435, 805)
    pyautogui.PAUSE = 1
    pyautogui.click(button='left')
    pyautogui.PAUSE = 4
    pyautogui.PAUSE = 4
    pyautogui.moveTo(545, 805)
    pyautogui.PAUSE = 1
    pyautogui.click(button='left')
    pyautogui.PAUSE = 4

def checkpixel(mouseX,mouseY,r ,g ,b):
    if pyautogui.pixelMatchesColor(mouseX, mouseY, (r, g, b),tolerance=10):
        return True
    else:
        return False

def oneturn():
    if checkpixel(1577,807,2,206,242):
        pyautogui.PAUSE = 4
        pyautogui.moveTo(1581, 843)
        pyautogui.PAUSE = 1
        pyautogui.click(button='left')
        pyautogui.PAUSE = 1.5
        pyautogui.moveTo(1600, 727)
        pyautogui.PAUSE = 1
        pyautogui.click(button='left')
        pyautogui.PAUSE = 1
        pyautogui.moveTo(1300, 727)
        pyautogui.PAUSE = 1
        pyautogui.click(button='left')
        pyautogui.PAUSE = 1
        pyautogui.moveTo(1000, 727)
        pyautogui.click(button='left')
        pyautogui.PAUSE = 1
        pyautogui.moveTo(700, 727)
        pyautogui.PAUSE = 1
        pyautogui.click(button='left')
        pyautogui.PAUSE = 1
        pyautogui.moveTo(400, 727)
        pyautogui.PAUSE = 1
        pyautogui.click(button='left')
        pyautogui.PAUSE = 16

def noble_phantasm():
    print("Prepara noble phantasm")
    skillUse()
    print("Usa noble phantasm")
    pyautogui.PAUSE = 5
    pyautogui.moveTo(1581, 843)
    pyautogui.PAUSE = 2
    pyautogui.click(button='left')
    pyautogui.PAUSE = 2
    pyautogui.moveTo(720, 380)
    pyautogui.PAUSE = 2
    pyautogui.click(button='left')
    pyautogui.PAUSE = 2
    pyautogui.moveTo(1000, 380)
    pyautogui.PAUSE = 2
    pyautogui.click(button='left')
    pyautogui.PAUSE = 2
    pyautogui.moveTo(1600, 727)
    pyautogui.PAUSE = 2
    pyautogui.click(button='left')
    pyautogui.PAUSE = 2
    pyautogui.moveTo(1300, 727)
    pyautogui.PAUSE = 2
    pyautogui.click(button='left')
    time.sleep(22)

def click_to_next_game():
    #Check gold letter Servant Bond
    if checkpixel(952,748,1,4,0):
        print("Click to next game ")
        pyautogui.PAUSE = 10
        pyautogui.moveTo(1000, 885)
        pyautogui.PAUSE = 3
        pyautogui.click(button='left')
        pyautogui.PAUSE = 3
        pyautogui.moveTo(1000, 885)
        pyautogui.PAUSE = 3
        pyautogui.click(button='left')
        pyautogui.PAUSE = 3
        print("Next Game")
        pyautogui.PAUSE = 3
        pyautogui.moveTo(1541, 930)
        pyautogui.PAUSE = 3
        pyautogui.click(button='left')
        pyautogui.PAUSE = 5
        print("Repeat Game")
        pyautogui.PAUSE = 5
        pyautogui.moveTo(1230, 800)
        pyautogui.PAUSE = 3
        pyautogui.click(button='left')
        pyautogui.PAUSE = 12
        no_stamina()
def no_stamina():
    if checkpixel(688,515,255,254,251):
        pyautogui.PAUSE = 2
        pyautogui.moveTo(688, 515)
        pyautogui.PAUSE = 2
        pyautogui.click(button='left')
        pyautogui.PAUSE = 12
        pyautogui.PAUSE = 5
        pyautogui.moveTo(1230, 800)
        pyautogui.PAUSE = 3
        pyautogui.click(button='left')
        pyautogui.PAUSE = 12
        print("Pick Servant")
        pyautogui.PAUSE = 3
        pyautogui.moveTo(960, 433)
        pyautogui.PAUSE = 2
        pyautogui.click(button='left')
        pyautogui.PAUSE = 10
    else:
        print("Pick Servant")
        pyautogui.PAUSE = 4
        pyautogui.moveTo(960, 433)
        pyautogui.PAUSE = 4
        pyautogui.click(button='left')
        pyautogui.PAUSE = 10

try:
    while True:
        pyautogui.PAUSE = 4
        if checkpixel(281,237,215,100,100):
            noble_phantasm()
        elif checkpixel(282,237,199,185,132):
            print("Revisando")
        elif checkpixel(1577,807,2,206,242):
            oneturn()
        elif checkpixel(366,347,232,184,32):
            click_to_next_game()
            repeat_game+=1
                
        
except KeyboardInterrupt:
    print("Numero de partidas "+str(repeat_game))
    print('\n') 

"""
pyautogui.moveTo(1581, 843)
pyautogui.click(button='left')
pyautogui.PAUSE = 1.5
pyautogui.moveTo(1600, 727)
pyautogui.PAUSE = 1
pyautogui.moveTo(1300, 727)
pyautogui.PAUSE = 1
pyautogui.moveTo(1000, 727)
pyautogui.PAUSE = 1
pyautogui.moveTo(700, 727)
pyautogui.PAUSE = 1
pyautogui.moveTo(400, 727)
pyautogui.PAUSE = 1

skills
x   y
325 805
435 805
545 805
x   y
700 805
810 805
920 805
x    y
1075 805
1185 805
1295 805

noble phantasm
 x    y
720  380
1000 380
1280 380
Check noble phantasm bar

end game 
1000 885 x2
1541 930 next
1230 795 repeat
960 433 clicl servant
wait load game
255 254 251 688 515 golden fruit
216 216 126 1179 197 next
65 40 170 550 468 servant pick
for x in range(6):


"""