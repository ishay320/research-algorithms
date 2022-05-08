import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

def plotIntersection(x, f, g):
    '''
    receive x space, function f and function g
    show graph
    '''
    # Plot the graph
    plt.plot(x, f(x), x, g(x))

    # Find and plot the dots
    for x0 in x:
        res = scipy.optimize.fsolve(lambda x : f(x) - g(x), x0,full_output=True)
        if(res[-1] == 'The solution converged.' and res[0] >= min(x) and res[0] <= max(x)):
            plt.plot(res[0],g(res[0]),'ro')

    # Show the graph
    plt.show()

if __name__ == "__main__":    
    #  Example 1
    x = np.linspace(-5,5,50)
    f = lambda x : x**2
    g = lambda x : x+3

    plotIntersection(x,f,g)

    #  Example 2
    x = np.linspace(-10,10,1000)
    f = lambda x : np.sin(x)
    g = lambda x : 0.2*x

    plotIntersection(x,f,g)

    #  Example 3
    x = np.linspace(-10,10,500)
    f = lambda x : np.sin(x)
    g = lambda x : np.cos(x)

    plotIntersection(x,f,g)
