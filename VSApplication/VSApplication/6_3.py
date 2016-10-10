# standard module containing clock function
import time

lastTime = time.clock()
curTime = 0

while(True):
    curTime = time.clock()
    nextTime = time.clock();

    diff = nextTime - curTime
    if diff > 20e-6:
        print("Took: {}".format(round(diff*1000000)))

    


