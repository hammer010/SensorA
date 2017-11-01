import time
 
def timer(length, dt=1): 
    end = time.time() + length 
    while(time.time() < end): 
        print "Only %.g more seconds!" % (end - time.time()) 
        time.sleep(dt) 
        print "Time's up!"
 
        else:
            print "Only %.1f more seconds!" % (length - (time.time() - start))
 
if __name__ == '__main__':
    timer(60)
