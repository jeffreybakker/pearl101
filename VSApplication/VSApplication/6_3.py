# standard module containing clock function
import time

lastTime = time.clock()
curTime = 0

while(True):
    curTime = time.clock()
    diff =  curTime - lastTime
    lastTime = curTime

    print("Took: {}".format(round(diff*1000000)))


