import time
import os  

 
def timer(length, dt=5): 
    end = time.time() + length 
    while(time.time() < end): 
        print "Only %.1f more seconds!" % (end - time.time())
        time.sleep(dt)
        os.system('clear')
        print "Fin"
if __name__ == '__main__':
    timer(300)
