from collections import defaultdict
import time
timing={}
agg = defaultdict(float)
def start(key):
    if  key not in timing:
        timing[key] = {'start':time.time() }
    else:
        timing[key]['start'] = time.time()

def end(key):
    timing[key]['end'] = time.time()
    agg[key] += timing[key]['end'] - timing[key]['start']

