import numpy as np 
import matplotlib.pyplot as plt 

# Functions
def sirkel(x: float, y: float, r: float) -> None : 
    t = np.linspace(0,2*np.pi,100)
    plt.plot(x+r*np.cos(t),y+r*np.sin(t),linewidth=2)

def plot_sirkler(matrix: list) -> None:
    y = 0
    for i in range(len(matrix)):
        x = matrix[i][i]
        r = np.sum(np.absolute(np.matrix(matrix[i]))) - abs(x)

        sirkel(x,y,r)
        
    plt.axis('equal')
    plt.savefig('Oppgave_1_plot')
    plt.show()

A = [[  -2,    0,  .5,  1],
     [-.25,    1, .25,  0],
     [   0,    0,   3, -1],
     [.125, .125, .25,  2]]


plot_sirkler(A)

