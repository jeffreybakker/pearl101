from collections import deque
import random

maxPackets = 100000
# the total amount of packets there are send.
totalPackets = 0
# The probability a computer is transmitting a packet
probability = 0.2
# The amount of computers that send packets
computerAmount = 4
ticks = 0

# the queue the router is using and which new packets are added to.
queue = deque([])

# the total waittime of all packets.
waitTime = 0

while totalPackets <= maxPackets:
    # update the ticks to the next one.
    ticks += 1

    i = 0
    # for every computer, send a packet
    while i < computerAmount:
        i += 1
        randomNumber = random.random()
        
        if randomNumber < probability:
            # We transmit the packet
            totalPackets+=1
            # The packet represents the tick at which the packet enters the queue.
            queue.append(ticks)
            if totalPackets > maxPackets:
                break

    if len(queue) > 0:
        # Add the waiting time of the current packet to the total waittime, used to calculate the average
        waitTime += ticks - queue.popleft()

# if there are still packets in the queue, keep finishing them
while len(queue) > 0:
    ticks+=1
    # Add the waiting time of the current packet to the total waittime, used to calculate the average
    waitTime += ticks - queue.popleft()

# Print the average waiting time
print(waitTime/totalPackets)
