import time
 
def timer(length, dt=1): 
    end = time.time() + length 
    while(time.time() < end): 
        print "Only %.1f more seconds!" % (end - time.time()) 
        time.sleep(dt) 
        print "Time's up!"
if __name__ == '__main__':
    timer(30)
