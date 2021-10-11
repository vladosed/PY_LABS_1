from math import factorial
from random import randint, randrange, sample, random   

#generate sequence from 4 numbers
seq_var1 = sample(range(0, 100), 5)
print(seq_var1)

#generate random float
rnd_flt = random()
print(rnd_flt)

#find max value from seqence
max_elem = max(seq_var1)
print(max_elem)

#floor division between max element and generated float
flr_div = max_elem // rnd_flt
print(flr_div)

#find factorial of the result above
print(factorial(flr_div))
