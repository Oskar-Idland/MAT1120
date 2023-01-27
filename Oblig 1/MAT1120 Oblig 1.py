import numpy as np 
import matplotlib.pyplot as plt 

# Functions
def sirkel(x: float, y: float, r: float, eig: tuple, sirkel_name: str) -> None : 
    t = np.linspace(0,2*np.pi,100)
    plt.plot(x+r*np.cos(t),y+r*np.sin(t),linewidth=2, label = sirkel_name)
    plt.scatter(eig[0], eig[1])

def egensirkler(matrix: list, filename: str) -> None:
    y = 0
    eigenvalues = np.linalg.eig(matrix)[0]
    for i in range(len(matrix)):
        sirkel_name = f'S{i+1}'
        eigReal, eigImag = eigenvalues[i].real, eigenvalues[i].imag
        x = matrix[i][i]
        r = np.sum(np.absolute(np.matrix(matrix[i]))) - abs(x)
        sirkel(x,y,r,(eigReal, eigImag), sirkel_name)
        
    plt.axis('equal')
    plt.legend()
    plt.savefig(filename)

#Matrixes

A = [[  -2,    0,  .5,  1],
     [-.25,    1, .25,  0],
     [   0,    0,   3, -1],
     [.125, .125, .25,  2]]

B = [[5, -1, 1],
     [1,  2, 1],
     [1, -1,-1]]

C = [[0,  3,  7,  1,  6],
     [7, 10,  1,  7,  9],
     [1,  8, 20,  1,  1],
     [1,  9,  3, 30,  3],
     [1,  7,  3,  2, 40]]

D = [[ 1, 0,  0,  0],
     [ 0, 6,  0,  0],
     [ 0, 0, 11,  0],
     [ 0, 0,  0, 16]]

# Function calls
egensirkler(A, 'Oppgave_3A_plot.pdf')
egensirkler(B, 'Oppgave_3B_plot.pdf')
egensirkler(C, 'Oppgave_3C_plot.pdf')
egensirkler(D, 'Oppgave_3D_plot.pdf')