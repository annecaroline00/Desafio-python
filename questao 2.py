import numpy as np 
vet = np.array([3**i + 7*np.math.factorial(i) if (i % 2 == 0) else (2**i + 4*np.math.log(i)) for i in range (0,11)])

print(np.where(vet == max(vet))[0][0])

print(round(np.mean(vet),2))
