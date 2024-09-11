def convolution(u,v):
    # Author: Francesco Straniero 21/01/2023
    # performs the convolution of two 1D signals, u and v
    # Input = two 1D numpy arrays 
    # Output = Graph of the convolved signal
    import numpy as np
    from scipy.fft import ifft
    import fft_function as func
    import matplotlib.pyplot as plt
    #First we perform the fourier transform of the input signals, we take the absolute value)
    ftu = abs(func.Fourier_transform(u))
    ftv = abs(func.Fourier_transform(v))
    l = np.size(u,0)
    #Then we multiply the two transforms
    fth = np.multiply(ftu,ftv)
    l = int(l)
    #Lastly we take the inverse Fourier transform to get the convolution in the signal space
    #Note that we add a reflected signal, this is because our DFT function had an output 
    # of the same size as the input, but for the convolution we want the output to be twice the size of the input 
    dl = 2*l
    ifth =np.zeros(dl)
    

    ifth[0:l] = ifft(fth, n = l)
    ifth[l:dl] = np.flip(ifft(fth, n = l))

    ifth = ifth[(l+1)//2:((3*l -1)//2)]
   
    plt.plot(ifth)
    plt.title("Single slit convolution")
    
