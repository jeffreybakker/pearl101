# standard module containing clock function
import time

lastTime = time.clock()
curTime = 0

while(True):
    curTime = time.clock()
    nextTime = time.clock()
    #diff =  curTime - lastTime
    #lastTime = curTime

    if(curTime - nextTime > 0):
        print("Took: {}".format(round(diff*1000000)))

    


