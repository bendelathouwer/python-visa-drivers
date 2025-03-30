import scope_wrapper
import matplotlib.pyplot as plt

Scope=scope_wrapper.Scope("TCPIP0::169.254.226.9::INSTR")
data= Scope.takemeasurement(" CHAN1","NORMal","ASCii")
plt.plot(data)#plt.plot takes an 1d np array and iterates over it by itself , no need to pass y values
plt.show()
