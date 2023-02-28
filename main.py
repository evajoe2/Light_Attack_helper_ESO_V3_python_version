
import pynput
from pynput.keyboard import Key, Listener, Controller as key_cl
from pynput.mouse import Button, Controller
import time
import random
from keymapping import*
import keymapping as km



#****************************************************************

show_esoass()
esomapping()
show_keyass()
remapping()

e_k1,e_k2,e_k3,e_k4,e_k5,e_k6 = show_esoass()
d_k1,d_k2,d_k3,d_k4,d_k5,d_k6 = show_keyass()

print("press home key to exit program")
time.sleep(0.5)

#****************************************************************

d_time = 0.08  # set ratio for delay time for light attack and skill
keyboard = key_cl()
mouse = Controller()

def m_ck():
    global ts
    mouse.press(Button.left)
    ts=round(d_time*(random.uniform(0.8, 1.1)), 2)
    time.sleep(ts)
    mouse.release(Button.left)
    
    
ignore_press = False
ignore_release = False

#*****************************************************************

def on_press(key):
    if key == Key.home:
        # Stop listener
        return False
    global ignore_press
    #************************************************* 
       
    if (key.char if hasattr(key, 'char') else key.name) == d_k1:
        if ignore_press:
            ignore_press = False
            return
        m_ck()
        keyboard.press(e_k1)
        keyboard.release(e_k1)
        print('added light Attack and delay '+ str(ts) + 'sec to skill 1')
        ignore_press = True
       
    if (key.char if hasattr(key, 'char') else key.name) == d_k2:
        if ignore_press:
            ignore_press = False
            return
        m_ck()
        keyboard.press(e_k2)
        keyboard.release(e_k2)
        print('added light Attack and delay '+ str(ts) + 'sec to skill 1')
        ignore_press = True    
       
    if (key.char if hasattr(key, 'char') else key.name) == d_k3:
        if ignore_press:
            ignore_press = False
            return
        m_ck()
        keyboard.press(e_k3)
        keyboard.release(e_k3)
        print('added light Attack and delay '+ str(ts) + 'sec to skill 3')
        ignore_press = True
       
    if (key.char if hasattr(key, 'char') else key.name) == d_k4:
        if ignore_press:
            ignore_press = False
            return
        m_ck()
        keyboard.press(e_k4)
        keyboard.release(e_k4)
        print('added light Attack and delay '+ str(ts) + 'sec to skill 4')
        ignore_press = True
       
    if (key.char if hasattr(key, 'char') else key.name) == d_k5:
        if ignore_press:
            ignore_press = False
            return
        m_ck()
        keyboard.press(e_k5)
        keyboard.release(e_k5)
        print('added light Attack and delay '+ str(ts) + 'sec to skill 5')
        ignore_press = True   
              
    if (key.char if hasattr(key, 'char') else key.name) == d_k6:
        if ignore_press:
            ignore_press = False
            return
        m_ck()
        print('light Attack added before ultimate skill')
        keyboard.press(e_k6)
        keyboard.release(e_k6)
        print('added light Attack and delay '+ str(ts) + 'sec to ultimate skill')
        ignore_press = True
#******************************************************

def on_release():
    return
    




with Listener(
        on_press=on_press,
        
        suppress=ignore_press) as ls:
    ls.join()



