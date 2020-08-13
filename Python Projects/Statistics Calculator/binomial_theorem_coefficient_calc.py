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
    power = int(input("Power of Binomial: "))
    coef_a = int(input("Coefficient of x or a: "))
    coef_b = int(input("Coefficient of y or b: "))

#Iterating the calc of coefficient in each term#
    for k in range(0, power+1):
        nCk = comb(power,k)
        coef = (coef_a**(power-k))*(coef_b**(k))*nCk
        print(k,": ", coef)



    
