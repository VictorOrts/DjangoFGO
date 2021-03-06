from logging import log
import pyautogui,sys
from loguru import logger

start_date= None
end_date = None
repeat_game = 0
match_value = 0.8
SHORT_TIME_WAIT = 3
MEDIUM_TIME_WAIT = 6
LONG_TIME_WAIT = 10

def skillUse(image):
    """
    x   y
    325 805 - 435 805 - 545 805
    x   y
    700 805 - 810 805 - 920 805
    x    y
    1075 805 - 1185 805 - 1295 805
    """
    for listPos in pyautogui.locateAllOnScreen(image,confidence=match_value):
        pyautogui.PAUSE = 2
        calculatemidx =listPos.left +(listPos.width*0.5)
        calculatemidy =listPos.top +(listPos.width*0.5)
        mouse_cycle(calculatemidx,calculatemidy)

    mouse_cycle(435, 805)
    mouse_cycle(545, 805)


def checkpixel(mouseX,mouseY,r ,g ,b):
    if pyautogui.pixelMatchesColor(mouseX, mouseY, (r, g, b),tolerance=10):
        return True
    else:
        return False

def oneturn():
    #Press Button Attack
    mouse_cycle(1581, 843)
    #Press x x x x X
    mouse_cycle_move_click(1600, 727,1)
    #Press x x x X x
    mouse_cycle_move_click(1300, 727,1)
    #Press x x X x x
    mouse_cycle_move_click(1000, 727,1)
    #Press x X x x x
    mouse_cycle_move_click(700, 727,1)
    #Press X x x x x
    mouse_cycle_move_click(400, 727,1)

def noble_phantasm():
    #Use Skill check buff attack
    #skillUse('img/atk_up.png')
    #Use Skill check buff attack
    #skillUse('img/quickup.png')
    #Use Skill check buff attack
    #skillUse('img/burst.png')
    #Press Button Attack
    mouse_cycle(1581, 843)
    #Press NP X x x 
    mouse_cycle_move_click(720, 380,1)
    #Press NP x X x 
    mouse_cycle_move_click(1000, 380,1)
    #Press NP x x X 
    mouse_cycle_move_click(1280, 380,1)
    #Press x x x x X
    mouse_cycle_move_click(1600, 727,1)
    #Press x x x X x
    mouse_cycle_move_click(1300, 727,1)
    #Press x x X x x
    mouse_cycle_move_click(1000, 727,1)
    pyautogui.PAUSE = LONG_TIME_WAIT

def mouse_cycle(x,y):
    pyautogui.PAUSE = SHORT_TIME_WAIT
    pyautogui.moveTo(x, y)
    pyautogui.PAUSE = SHORT_TIME_WAIT
    pyautogui.click(button='left')
    pyautogui.PAUSE = MEDIUM_TIME_WAIT

def mouse_cycle_move_click(x,y,time):
    pyautogui.PAUSE = time
    pyautogui.moveTo(x, y)
    pyautogui.PAUSE = time
    pyautogui.click(button='left')
    pyautogui.PAUSE = time

def mouse_cycle_short_long(x,y):
    pyautogui.PAUSE = SHORT_TIME_WAIT
    pyautogui.moveTo(x, y)
    pyautogui.PAUSE = SHORT_TIME_WAIT
    pyautogui.click(button='left')
    pyautogui.PAUSE = LONG_TIME_WAIT

def click_to_next_game():
    #Check gold letter Servant Bond
    if pyautogui.locateOnScreen('img/next.png',confidence=match_value):
        x,y = pyautogui.locateCenterOnScreen('img/next.png',confidence=match_value)
        mouse_cycle(x,y)
    if pyautogui.locateOnScreen('img/repeat.png',confidence=match_value):
        x,y = pyautogui.locateCenterOnScreen('img/repeat.png',confidence=match_value)
        mouse_cycle(x,y)
        check_stamina()

def check_stamina():
    pyautogui.PAUSE = 3
    if  pyautogui.locateOnScreen('img/goldenapple.png',confidence=match_value):
        pyautogui.PAUSE = 2
        x,y = pyautogui.locateCenterOnScreen('img/goldenapple.png',confidence=match_value)
        mouse_cycle(x,y)
        x,y = pyautogui.locateCenterOnScreen('img/ok.png',confidence=match_value)
        mouse_cycle_short_long(x,y)
        logger.info("Pick Servant")
        pyautogui.PAUSE = 4
        mouse_cycle_short_long(960,433)
    else:
        logger.info("Pick Servant")
        pyautogui.PAUSE = 5
        #x,y = pyautogui.locateCenterOnScreen('img/Confirmss.png',confidence=match_value)
        mouse_cycle_short_long(960,433)



try:
    logger.add("test1.log")
    #logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")
    logger.debug("STARTING BOT")
    while True:
        pyautogui.PAUSE = 2
        if pyautogui.locateOnScreen('img/cara.png',confidence=match_value):
            
            if pyautogui.locateOnScreen('img/round3.png',confidence=match_value) and pyautogui.locateOnScreen('img/danger.png',confidence=match_value):
                logger.info("Noble Phantasm")
                noble_phantasm()
            elif pyautogui.locateOnScreen('img/round3event.png',confidence=match_value) and pyautogui.locateOnScreen('img/servantchecknp.png',confidence=match_value):
                logger.info("Noble Phantasm Event")
                noble_phantasm()
            elif pyautogui.locateOnScreen('img/round3.png',confidence=match_value) and pyautogui.locateOnScreen('img/servantcheckrice.png',confidence=match_value):
                logger.info("Noble Phantasm Event rice")
                noble_phantasm()
            #elif pyautogui.locateOnScreen('img/attack.png',confidence=match_value):
            elif pyautogui.locateOnScreen('img/cara.png',confidence=match_value):
                logger.info("Turno")
                oneturn()
            
        elif pyautogui.locateOnScreen('img/servantbond.png',confidence=match_value):
            #click_to_next_game()
            logger.info("Check Servant Bond Image")
            x,y = pyautogui.locateCenterOnScreen('img/servantbond.png',confidence=match_value)
            mouse_cycle(x,y)
            repeat_game+=1
        elif pyautogui.locateOnScreen('img/expgained.png',confidence=match_value):
            #click_to_next_game()
            logger.info("Check Exp Gained Image")
            x,y = pyautogui.locateCenterOnScreen('img/expgained.png',confidence=match_value)
            mouse_cycle(x,y)
        elif pyautogui.locateOnScreen('img/motivation.png',confidence=match_value):
            #click_to_next_game()
            logger.info("Motivation")
            x,y = pyautogui.locateCenterOnScreen('img/next.png',confidence=match_value)
            mouse_cycle(x,y)
        elif pyautogui.locateOnScreen('img/imagination.png',confidence=match_value):
            #click_to_next_game()
            logger.info("Imagination")
            x,y = pyautogui.locateCenterOnScreen('img/next.png',confidence=match_value)
            mouse_cycle(x,y)
        elif pyautogui.locateOnScreen('img/magifd.png',confidence=match_value):
            #click_to_next_game()
            logger.info("Tecnica")
            x,y = pyautogui.locateCenterOnScreen('img/next.png',confidence=match_value)
            mouse_cycle(x,y)
        elif pyautogui.locateOnScreen('img/itemsdropped.png',confidence=match_value):
            logger.info("Check Items Dropped Image")
            x,y = pyautogui.locateCenterOnScreen('img/next.png',confidence=match_value)
            mouse_cycle(x,y)
        elif pyautogui.locateOnScreen('img/repeat.png',confidence=match_value):
            x,y = pyautogui.locateCenterOnScreen('img/repeat.png',confidence=match_value)
            mouse_cycle(x,y)
            check_stamina()
                
        
except KeyboardInterrupt:
    logger.info("Termino el bot -> ")
    logger.info("Numero de partidas "+str(repeat_game))
