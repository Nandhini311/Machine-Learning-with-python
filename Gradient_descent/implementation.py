import numpy as np

def gradient_descent(x,y):
    m_curr = b_curr = 0
    iterations = 1000
    n = len(x)
    learning_rate = 0.0001
    #take baby steps to reach global minima
    
    for i in range(iterations):
        y_predicted = m_curr*x + b_curr
        md = -(2/n)*sum(x*(y-y_predicted)) #n-length of data points
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate*md
        b_curr = b_curr - learning_rate*bd
        print("m {} b{} iterations {}".format(m_curr,b_curr,iterations))
        
        
x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)
