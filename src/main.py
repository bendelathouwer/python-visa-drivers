
import scoop_wrapper
import matplotlib.pyplot as plt
#plotting needs figuering out the plotting
data= []
scoop=scoop_wrapper.scoop("TCPIP0::169.254.226.8::INSTR")
data = scoop.takemeasurement("CHAN1","NORMal","ASCii")
print(data)
print(type(data))
print(len(data))
fig, ax = plt.subplots()             # Create a figure containing a single Axes.


for i in range (len(data)):
    ax.plot(i, data)
plt.show()
