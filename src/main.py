
import scoop_wrapper
import matplotlib.pyplot as plt
import numpy as np

scoop=scoop_wrapper.scoop("TCPIP0::169.254.226.9::INSTR")
data= scoop.takemeasurement("CHAN1","NORMal","ASCii")
index= np.nditer(data)
plt.plot(data,len(index))
plt.show()
