
import scoop_wrapper
data= []
scoop=scoop_wrapper.scoop("TCPIP0::169.254.226.8::INSTR")
data = scoop.takemeasurement("CHAN1","NORMal","ASCii")
print(data)
print(type(data))