
import scoop_wrapper
import matplotlib.pyplot as plt
import numpy as np

scoop=scoop_wrapper.scoop("TCPIP0::169.254.226.9::INSTR")
data = scoop.takemeasurement("CHAN1","NORMal","ASCii")
print(data)
print(type(data))
print(len(data))
newdata=data[11:len(data)]
print(newdata)
ax,fig =plt.subplots()
plt.plot([len(newdata)],[newdata])
plt.show()
