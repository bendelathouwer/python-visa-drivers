
import scoop_wrapper
import matplotlib.pyplot as plt
import numpy as np
data = []
scoop=scoop_wrapper.scoop("TCPIP0::169.254.226.9::INSTR")
data= scoop.takemeasurement("CHAN1","NORMal","ASCii")
<<<<<<< HEAD
print(data)
print(type(data))
print(len(data))
plt.plot(np.arange(data),data)
=======
index= np.nditer(data)
plt.plot(data,len(index))
>>>>>>> 80e08591312b2314fbb4f58aea85b71c7c0ebbd7
plt.show()
