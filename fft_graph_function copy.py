def Fourier_transform_graphs(X):
    # Author: Francesco Straniero 21/01/2023
    # Fourier transform function for a 1d signal.
    # Input: 1D vector of N elements
    # Output: graphs of the original signal, the real Fourier transform and the Standard Fourier transform.
    
    import numpy as np
    import matplotlib.pyplot as plt
    import math
    plt.plot(X)
    plt.title('Signal')
    plt.show()

    l = len(X)
    ff = np.zeros(2*l)

    ff[0:l] = X

    ff[l:2*l] = np.flip(X)
    

    RF = np.zeros(l)
    IF = np.zeros(l)
    real = np.zeros(2*l)
    imag = np.zeros(2*l)
    for u in range(l):
        for i in range(2*l):
            if i<l:
                real[i] = ff[i]*math.cos((np.pi)*i*u/l)
                imag[i] = ff[i]*math.sin((np.pi)*i*u/l)
            else:
                real[i] = ff[i]*math.cos(-(np.pi)*i*u/l)
                imag[i] = ff[i]*math.sin(-(np.pi)*i*u/l)
            
        RF[u] = np.sum(real)
        IF[u] = np.sum(imag)
    plt.plot(RF)
    plt.title('Real part of the DFT')
    plt.show()

    TT = RF+IF
    plt.plot(TT)
    plt.title('DFT')
    plt.show()
