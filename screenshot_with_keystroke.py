from pynput import mouse
from pynput import keyboard
from pynput.keyboard import Listener
import pyautogui
import ctypes  # An included library with Python install.   
import os
import datetime

ctypes.windll.user32.MessageBoxW(0, "clique em 3 vertices da região a gravar!", "Defina a Região!", 1)

base_path = "C:/prints/"
folder=datetime.datetime.now().strftime('%Y_%m_%d_%H_%M%S')
full_path=base_path+folder
region=[[],[]]  #for coordinates

print_nr=1

os.mkdir(full_path)



#Define region to print  
def on_click(x, y, button, pressed):
    if pressed:
        region[0].append(x)
        region[1].append(y)
    print('{0} at {1}'.format( 'Pressed' if pressed else 'Released',(x, y)))
    if len(region[0])>2:
        print(region)
        return False

def on_press(key):
    def get_coordinates():
        x_max=max(region[0])
        x_min=min(region[0])

        y_max=max(region[1])
        y_min=min(region[1])
        return x_min, y_min, x_max, y_max


    def take_screenshot( coordinates):
        global print_nr
        im = pyautogui.screenshot(region= coordinates)
        im.save(r'{}/{}.png'.format(full_path,print_nr))
        print_nr+=1


    if key == keyboard.Key.esc:
        ctypes.windll.user32.MessageBoxW(0,  " prints guardados em: {}".format(full_path), "Terminado!", 1)
        return False
    if key.char == ('p'):
        take_screenshot( get_coordinates ())    


with mouse.Listener(on_click = on_click) as listener:
    listener.join()

ctypes.windll.user32.MessageBoxW(0, "Pressione p para gurdar um print","Aviso! ",  1)

with keyboard.Listener(on_press = on_press) as key_listener:
    key_listener.start
    key_listener.join()

