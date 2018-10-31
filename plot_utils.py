'''
very simple shortcuts for making plots
'''
import matplotlib.pyplot as plt
def new_column(nrow, xlim):
    '''
    a single column with multiple rows
    '''
    f, ax = plt.subplots(nrow, 1, figsize = (6, 1+3*nrow))
    plt.subplots_adjust(hspace = 0)
    for i in range(nrow):
        ax[i].set_xlim(xlim)
        ax[i].tick_params(labelsize = 18)
        if i != nrow - 1:
            ax[i].set_xticklabels([])
    return f, ax