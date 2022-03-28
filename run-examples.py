# Explanation:

'''
the main idea of the paper is compering run time of different algorithm
and showing that the old BC is the best if we wse the paper improvement (IBC). 
'''


'''
we have 2 type of algorithm runtime
and both of them use the same input but:
'''

'''
# Bin Packing
we choose random variabels.
we have C that stand for capacity of the bin.
we have E[B] is he expected number of bins in an optimal partition given the range. <- what the algo search for

the algorithm we have: BC, BCP, IBC
## Example:
var = {1,4,3,3,4,2}
C = 5
E[B] = 4  // (because [1,4],[3,2],[4],[3])
now we need to check for time between algorithm
'''

'''
# Number Partitioning
we choose random variabels.
we have k is the number of bins.
we have C that stand for capacity of the bin that the algorithm expect. <- what the algo search for 

the algorithm we have: BSBCP, BSIBC
## Example:
var = {1,4,3,3,4,2}
k = 4  
C = 5 // (because [1,4],[3,2],[4],[3])
now we need to check for time between algorithm
'''

## The examples:
### every one is 2 types of testing and based on that all the testing will be perform

# Bin Packing - check correctness and time
''' 
import time
import numpy as np

n = 45
max_range = 500,000
min_range = 1
var = [np.random.randint(low=min_range, high=max_range,) for x in range(n)]
C = 10**6
E[B] = ((max_range)*n) / 2C # the expectation

start_time_BC = time.time()
assert len(BC(var, C)) == E[B] # check if the number of bins correct
end_time_BC = time.time()

start_time_IBC = time.time()
assert len(IBC(var, C)) <= E[B] # check if the number of bins correct
end_time_IBC = time.time()

start_time_BCP = time.time()
assert len(BCP(var, C)) <= E[B] # check if the number of bins correct
end_time_BCP = time.time()

time_BC =  end_time_BC - start_time_BC
time_IBC =  end_time_IBC - start_time_IBC
time_BCP =  end_time_BCP - start_time_BCP

# Check the timeing
assert time_BC > time_BCP
assert time_BCP > time_IBC

## edge cases:
For E[B] > 22, IBC no longer completes all it's experiments
within 24 hour limit while BCP successfully solves
all problems.
'''

# Number Partitioning - check correctness and time
''' 
import time
import numpy as np

n = 45
max_range = 500,000
min_range = 1
var = [np.random.randint(low=min_range, high=max_range,) for x in range(n)]
k = 6
C = 10**6 # the expectation

# TODO: separate the timing from the assert (its here for convenience)
start_time_BSIBC = time.time()
assert max([sum(x) for x in BSIBC(var, k)]) <= C # check if the capacity correct
end_time_BSIBC = time.time()

start_time_BSBCP = time.time()
assert max([sum(x) for x in BSBCP(var, k)]) <= C # check if the capacity correct
end_time_BSBCP = time.time()

time_BSIBC =  end_time_BSIBC - start_time_BSIBC
time_BSBCP =  end_time_BSBCP - start_time_BSBCP

# Check the timeing
assert time_BSBCP > time_BSIBC

## edge cases:
k = 9 and C = 10**6 BSBCP > BSIBC # from the paper

'''