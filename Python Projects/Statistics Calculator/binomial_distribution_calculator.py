import math

#Using the formula of combination and defining combination#
def comb(n,k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

Run = True

while Run:
#Control-Flow
    run_or_stop = str(input("Still want to run in next calculation? (Y/N):  "))
    if run_or_stop == 'N':
        Run = False
#Inputs
    print('-------------')
    n = int(input("Number of trials: "))
    print('-------------')
    p = float(input("Probability of Success: "))
    print('-------------')
    x = int(input("Number of Successes: "))
    print('-------------')
#Iterating the calc of coefficient in each term#
    nCx = comb(n,x)
    result = nCx * (p**x) * ((1-p)**(n-x))
    print(result)