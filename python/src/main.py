"""demo programe for the scope wrapper"""
import matplotlib.pyplot as plt
import scope_wrapper


Scope=scope_wrapper.Scope("TCPIP0::169.254.226.8::INSTR")
data= Scope.takemeasurement(" CHAN1","NORMal","ASCii")
#plt.plot takes an 1d np array and iterates over it by itself , no need to pass y values
plt.plot(data)
plt.show()
