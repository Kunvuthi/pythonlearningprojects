import math

#Using the formula of combination and defining combination#
def comb(n,k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))


def solve(n,p,x):
    result = 0
    for i in range(x):
        nCx = comb(n,i)
        result += nCx * (p**i) * ((1-p)**(n-i))
        print('P(X <=', i, ')', '=', result)

solve(50, 0.05, 5)


