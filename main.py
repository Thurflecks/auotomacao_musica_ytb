import pyautogui
import time


musica = input("qual a musica deseja ouvir? ")

if musica =='':
    print('Você não digitou uma música')
    exit()

pyautogui.PAUSE = 1.5
pyautogui.hotkey("ctrl" + "alt"+ "t")
pyautogui.write("brave-browser")
pyautogui.press('enter')
pyautogui.write('youtube.com')
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=814, y=133)
pyautogui.write(musica)
pyautogui.press('enter')
pyautogui.click(x=740, y=349)