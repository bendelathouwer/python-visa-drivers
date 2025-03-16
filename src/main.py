
import scoop_wrapper
import matplotlib.pyplot as plt
scoop=scoop_wrapper.scoop("TCPIP0::169.254.226.9::INSTR")
data= scoop.takemeasurement("CHAN1","NORMal","ASCii")
plt.plot(data)#plt.plot takes an 1d np array and iterates over it by itself , no need to pass y values
plt.show()
