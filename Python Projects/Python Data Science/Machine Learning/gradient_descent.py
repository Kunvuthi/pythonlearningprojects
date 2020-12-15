import math
import numpy as np


def gradient_descent(x, y):
    b_current = m_current = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.0306

    for i in range(iterations):
        y_predicted = m_current*x + b_current    
        ## Cost Function ##
        cost_func = (1/n)*(sum([val**2 for val in (y-y_predicted)]))

        ## Derivative of Cost Function with Respect to m, b ##
        d_dm = (-2/n)*sum(x*(y-y_predicted))
        d_db = (-2/n)*sum(y-y_predicted)

        ## Updating m, b values to converge ## 
        m_current = m_current - (learning_rate*d_dm)
        b_current = b_current - (learning_rate*d_db)        
        print("m: {}, b: {}, cost: {}, iteration: {}".format(m_current, b_current, cost_func, i))



x = np.array([i for i in range(1, 10)])
y = np.array([2,4,5,7,9,9,11, 13, 15])

gradient_descent(x, y)



