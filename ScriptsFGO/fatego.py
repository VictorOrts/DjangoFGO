import pyautogui, sys, time
repeat_game = 0
match_value = 0.8
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
    print("Turno !")
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
    pyautogui.PAUSE = 1
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
    #skillUse()
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
    pyautogui.PAUSE = 2
    pyautogui.moveTo(1000, 727)
    pyautogui.PAUSE = 2
    pyautogui.click(button='left')
    pyautogui.PAUSE = 2
    time.sleep(22)

def click_to_next_game():
    #Check gold letter Servant Bond
    if pyautogui.locateOnScreen('next.png',confidence=match_value):
        x,y = pyautogui.locateCenterOnScreen('next.png',confidence=match_value)
        pyautogui.PAUSE = 3
        pyautogui.moveTo(x, y)
        pyautogui.PAUSE = 3
        pyautogui.click(button='left')
        pyautogui.PAUSE = 3
        print("Repeat Game")
        pyautogui.PAUSE = 3
    if pyautogui.locateOnScreen('repeat.png',confidence=match_value):
        x,y = pyautogui.locateCenterOnScreen('repeat.png',confidence=match_value)
        pyautogui.moveTo(x, y)
        pyautogui.PAUSE = 3
        pyautogui.click(button='left')
        pyautogui.PAUSE = 12
        no_stamina()

def no_stamina():
    if  pyautogui.locateOnScreen('goldenapple.png',confidence=match_value):
        pyautogui.PAUSE = 2
        x,y = pyautogui.locateCenterOnScreen('goldenapple.png',confidence=match_value)
        pyautogui.PAUSE = 2
        pyautogui.moveTo(x, y)
        pyautogui.PAUSE = 2
        pyautogui.click(button='left')
        pyautogui.PAUSE = 10
        x,y = pyautogui.locateCenterOnScreen('ok.png',confidence=match_value)
        pyautogui.PAUSE = 5
        pyautogui.moveTo(x, y)
        pyautogui.PAUSE = 5
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
        if pyautogui.locateOnScreen('attack.png',confidence=match_value):
            #noble_phantasm()
            print("Attack Select")
            if pyautogui.locateOnScreen('round3.png',confidence=match_value):
                noble_phantasm()
            elif pyautogui.locateOnScreen('attack.png',confidence=match_value):
                oneturn()
            
        elif pyautogui.locateOnScreen('servantbond.png',confidence=match_value):
            #click_to_next_game()
            print("Servant Bond")
            x,y = pyautogui.locateCenterOnScreen('servantbond.png',confidence=match_value)
            pyautogui.PAUSE = 5
            pyautogui.moveTo(x, y)
            pyautogui.PAUSE = 5
            pyautogui.click(button='left')
            pyautogui.PAUSE = 5
            repeat_game+=1
        elif pyautogui.locateOnScreen('expgained.png',confidence=match_value):
            #click_to_next_game()
            print("Exp Gained")
            x,y = pyautogui.locateCenterOnScreen('expgained.png',confidence=match_value)
            pyautogui.PAUSE = 3
            pyautogui.moveTo(x, y)
            pyautogui.PAUSE = 3
            pyautogui.click(button='left')
            pyautogui.PAUSE = 3
        elif pyautogui.locateOnScreen('itemsdropped.png',confidence=match_value):
            print("Items dropped")
            click_to_next_game()
                
        
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