import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


M = 10  # No. of weights of the filter
w = np.zeros(M)  # Initializing the filter weights
mu = 0.0001  # step size

#Reading the speech and noise data
d,fs = sf.read('Record-001.wav')
v,fs = sf.read('Record-002.wav')
#print(v)
#print(d)
#print(fs)
#print np.var(v)

#In case of number of samples data is not equal
if(len(d) <= len(v)):
	N = len(d)
else:
	N = len(v)
#print(N)

e = np.zeros(N) # error signal
y = np.zeros(N) # Output of the filter
u = np.concatenate((np.zeros(M-1),v))	

# LMS Algorithm
for i in range(N):
	x = np.flipud(u[i:i+M])
	#print(np.shape(z))
	#d = np.flipud(x[i:i+filtlen])
	y[i] = np.sum(w*x)
	e[i] = d[i] - y[i]
	#print(e[i])
	w += mu*e[i]*x   #Update weights
	
S_hat = e
sf.write('output_signal_lms1.wav', S_hat,fs)
	
