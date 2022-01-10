import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


d,fs = sf.read('signal_noise.wav')
v,fs = sf.read('noise.wav')
print(d)
print(np.shape(v))
print(fs)

if(len(d) <= len(v)):
	N = len(d)
else:
	N = len(v)
#print(N)

filtlen = 10
w = np.zeros(filtlen)
mu = 0.01
e = np.zeros(N)
y = np.zeros(N)
for i in range(N):
	if(i-filtlen >= 0):
		for j in range(filtlen):
			e[i] += v[i-j] * w[j]
	else:
		for j in range(i):
			e[i] += v[i-j] * w[j]		
			
	y[i] = d[i] - e[i]
	
	for k in range(filtlen):
		w[k] = w[k] + mu*y[i]*v[i-k]
	
sf.write('output_signal_lms.wav',y,fs)
	
			

	
