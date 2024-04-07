# Implementation of matplotlib function 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 

def main():
    plot_contour("horizontal_survey_g1.csv",7.5)
    plot_contour("horizontal_survey_g2.csv",19.5)
    plot_contour("horizontal_survey_g3.csv",19.5)

def plot_contour(file,depth):
    """
    takes file name that should be in csv format x, y, z with z being a value at x and y and plots a contour
    first row should have x,y,z
    """
    depth = str(depth)
    contour_data = pd.read_csv(file)
    Z = contour_data.pivot_table(index='x',columns='y',values='z').T.values
    X_u = np.sort(contour_data.x.unique())
    Y_u = np.sort(contour_data.y.unique())
    X,Y = np.meshgrid(X_u,Y_u)
    fig, ax = plt.subplots(1, 1) 
    # C = ax.contour(X, Y, Z) 
    # plt.clabel(C, inline =1, fontsize=10)
    C = ax.contourf(X, Y, Z) 
    fill_label, labels = C.legend_elements()
    ax.legend(fill_label,[f"{L:.{1}f}"+ " Ωm" for L in C.levels])
    fig_name = file[0:-4]      
    ax.set_title('Contour Plot At Depth: '+depth+' [cm] \n'+fig_name) 
    ax.set_xlabel('x [cm]') 
    ax.set_ylabel('y [cm]') 
    plt.savefig(fig_name)
if __name__ == "__main__":
    main()
