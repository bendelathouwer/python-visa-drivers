import scope_wrapper
import matplotlib.pyplot as plt

scope=scope_wrapper.scope("TCPIP0::169.254.226.9::INSTR")
data= scope.takemeasurement(" CHAN1","NORMal","ASCii")
plt.plot(data)#plt.plot takes an 1d np array and iterates over it by itself , no need to pass y values
plt.show()
