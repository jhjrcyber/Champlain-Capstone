import math
import random
import itertools


def find_period(a,N):
    for r in itertools.count(start=1):
        if a**r % N == 1:
            return r

def shors_algorithm(N):
    assert(N > 0)
    assert(int(N)==N)
    while True:
        a = random.randint(0,N-1)
        g=math.gcd(a,N)
        if g!=1 or N==1:
            first_factor=g
            second_factor=int(N/g)
            return first_factor,second_factor
        else:
            r=find_period(a,N) 
            if r % 2 != 0:
                continue
            elif a**(int(r/2)) % N == -1 % N:
                continue
            else:
                first_factor=math.gcd(a**int(r/2)+1,N)
                second_factor=math.gcd(a**int(r/2)-1,N)
                if first_factor==N or second_factor==N:
                    continue
                return first_factor,second_factor

N=int(input("Interger to be factored:"))

print('\n Shors Algorithm')
print('--------------------')
print('\nExecuting...\n')

print(shors_algorithm(N))
