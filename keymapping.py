import time
import csv


def show_keyass():

    with open('keymap.csv') as fr:
        km_r = csv.reader(fr, delimiter=',')
        for row in km_r:
            d_k1, d_k2, d_k3, d_k4, d_k5, d_k6 = (row)
            print("Now the python key setting are \n skill 1 = " + d_k1 + ", skill 2 = " +
                  d_k2 + ", skill 3 = " + d_k3 + ', skill 4 = ' + d_k4 + ', skill 5 = '+d_k5 + ',ultimate on '+d_k6+' \n')  
    return d_k1, d_k2, d_k3, d_k4, d_k5, d_k6     
    
    

def show_esoass():

    with open('GameKeymap.csv') as er:
        wm_r = csv.reader(er, delimiter=',')
        for row in wm_r:
            e_k1, e_k2, e_k3, e_k4, e_k5, e_k6 = (row)
            print("Now the ESO game setting are \n skill 1 = " + e_k1 + ", skill 2 = " +
                  e_k2 + ", skill 3 = " + e_k3 + ', skill 4 = ' + e_k4 + ', skill 5 = '+e_k5 + ',ultimate on '+e_k6+' \n')
            
    return e_k1, e_k2, e_k3, e_k4, e_k5, e_k6        
    

def remapping():
    
    Remapkey = input("do you want to re-map Python keys ? y or n: \n")
    if Remapkey == 'y':
        d_k1 = input("skill 1 = ?  ")
        d_k2 = input("skill 2 = ?  ")
        d_k3 = input("skill 3 = ?  ")
        d_k4 = input("skill 4 = ?  ")
        d_k5 = input("skill 5 = ?  ")
        d_k6 = input("ultimate on = ?  ")       
        with open('keymap.csv', 'w', newline='') as fw:
            dwriter = csv.writer(fw)
            dwriter.writerow([d_k1, d_k2, d_k3, d_k4, d_k5, d_k6])
        show_keyass()
    else:
        print()
        time.sleep(0.5)
        return
       
def esomapping():
    
    Remap_eso = input("do you want to mapping ESO keys ? y or n: \n")
    if Remap_eso == 'y':
        e_k1 = input("skill 1 = ?  ")
        e_k2 = input("skill 2 = ?  ")
        e_k3 = input("skill 3 = ?  ")
        e_k4 = input("skill 4 = ?  ")
        e_k5 = input("skill 5 = ?  ")
        e_k6 = input("ultimate on = ?  ")      
        with open('GameKeymap.csv', 'w', newline='') as ew:
            dwriter = csv.writer(ew)
            dwriter.writerow([e_k1, e_k2, e_k3, e_k4, e_k5, e_k6])
        show_esoass()
    else:
        print()
        time.sleep(0.5)
        return