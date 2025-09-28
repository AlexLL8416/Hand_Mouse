import pyautogui

#pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = False

def moveRaton(posicion_x,posicion_y,anchura_camara,altura_camara):
    anchura_pantalla, altura_pantalla = pyautogui.size()
    pyautogui.moveTo(1.125*posicion_x*anchura_pantalla/anchura_camara,1.125*posicion_y*altura_pantalla/altura_camara)
    return None

def clickRaton():
    pyautogui.click()