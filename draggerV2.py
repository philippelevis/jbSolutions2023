from pynput import mouse
from pynput import keyboard
import time
mcontr = mouse.Controller()
running = True
toggled = False
active = False
def on_click(x, y, button, pressed):
    global active
    if button == mouse.Button.button8:
        #print('activating', pressed)
        active = pressed

def on_press(key):
    global toggled
    #print(str(key))
    if str(key) == "'r'":
        print('toggling')
        toggled = not toggled

listener = mouse.Listener(on_click=on_click)
listener.start()
kblistener = keyboard.Listener(on_press=on_press)
kblistener.start()

while running:
    if toggled:
        if active:
            mcontr.click(mouse.Button.right, 1)
            time.sleep(0.025)