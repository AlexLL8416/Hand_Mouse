import pyautogui

#pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = False

def moveRaton(posicion_x,posicion_y,anchura_camara,altura_camara):
    anchura_pantalla, altura_pantalla = pyautogui.size().width, pyautogui.size().height
    pyautogui.moveTo(posicion_x*anchura_pantalla/anchura_camara,posicion_y*altura_pantalla/altura_camara)
    return None
