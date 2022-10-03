from pypresence import Presence
import time
import random

client_id = 'yourclientID'
RPC = Presence(client_id) 
RPC.connect() 


count = 0
while True:
    with open ("lyrics.txt") as f:
        Lines = f.readlines()
        for line in Lines:
            count += 1
            print("Line{}: {}".format(count, line.strip()))
            RPC.update(state=line)
            
            time.sleep(3) #Wait a wee bit
        
