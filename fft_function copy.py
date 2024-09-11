def Fourier_transform(X):
    # Author: Francesco Straniero 21/01/2023
    # Fourier transform function for a 1d signal.
    # Input: 1D vector of N elements
    # Output: 1D array with complex coeffs of the fourier transform
    import numpy as np
    import math 

    l = len(X)              # Gets the lenght of the array
    ff = np.zeros(2*l)

    ff[0:l] = X 
    ff[l:2*l] = np.flip(X)   # The DFT needs to take both the input signal and its reflection
                             # This is to avoid edge effects
    

    RF = np.zeros(l)
    IF = np.zeros(l)
    FT = np.zeros(l)
    real = np.zeros(2*l)
    imag = np.zeros(2*l)
    #Use a double for loop to perform operation over i elements of input array 
    # to fill u elements of RF and IF arrays
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
    IF = IF*1j #Makes IF array imaginary
    FT = np.add(RF,IF) #FT is now complex
    return  FT