from http.client import OK
import os
import sys
from time import time
import numpy as np


raw_dataset_dir = sys.argv[1]

traces = os.listdir(raw_dataset_dir)
if not os.path.exists('./norway-processed'):
    os.mkdir('./norway-processed')

for trace in traces:
    print(trace)
    raw_trace = np.loadtxt(os.path.join(raw_dataset_dir, trace))
    timestamps = raw_trace[:, 0]
    timestamps -= np.min(timestamps)
    throughput_mbit = raw_trace[:, 4] * 8.0 / 1000000.0
    trace_processed = np.vstack([timestamps, throughput_mbit]).T
    print(trace_processed.shape)
    np.savetxt(os.path.join('norway-processed', trace), trace_processed, fmt='%3f')
