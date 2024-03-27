# Implementation of matplotlib function 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 

def main():
# Creating 2-D grid of features 
    contour_data = pd.read_csv("data.txt")
    Z = contour_data.pivot_table(index='x',columns='y',values='z').T.values
    X_u = np.sort(contour_data.x.unique())
    Y_u = np.sort(contour_data.y.unique())
    X,Y = np.meshgrid(X_u,Y_u)
    fig, ax = plt.subplots(1, 1) 
    ax.contourf(X, Y, Z) 
      
    ax.set_title('Contour Plot') 
    ax.set_xlabel('x [cm]') 
    ax.set_ylabel('y [cm]') 
    plt.savefig("group3contour")
if __name__ == "__main__":
    main()
