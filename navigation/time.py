import time

program_starts = time.time()
while(True):
    now = time.time()
    print("It has been {0} seconds since the loop started".format(now - program_starts))
