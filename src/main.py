
import scoop_wrapper
import matplotlib.pyplot as plt
import numpy as np
data = []
scoop=scoop_wrapper.scoop("TCPIP0::169.254.226.9::INSTR")
data= scoop.takemeasurement("CHAN1","NORMal","ASCii")
print(data)
print(type(data))
print(len(data))
plt.plot(np.arange(data),data)
plt.show()
