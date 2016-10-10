# standard module containing clock function
import time

while(True):
    start = time.clock()

    #do stuff
    counting = 0
    while(counting<=1000000):
        counting+=1

    duration = time.clock() - start
    print("Took: {}".format(round(duration*1000000)))


