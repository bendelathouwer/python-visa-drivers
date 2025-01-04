
import scoop_wrapper
import matplotlib.pyplot as plt
import numpy as np
#plotting needs figuering out the plotting

scoop=scoop_wrapper.scoop("TCPIP0::169.254.226.8::INSTR")
data = scoop.takemeasurement("CHAN1","NORMal","ASCii")
print(data)
print(type(data))
print(len(data))
t = np.arange(0, len(data))
fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([data], [len(data)])  # Plot some data on the Axes.
plt.show()

