import scoop_wrapper
import time
scoop=scoop_wrapper.scoop("TCPIP0::169.254.226.8::INSTR")
channel=4
scoop.setchannelcoupling(channel,"AC")
time.sleep(5)
scoop.setchannelcoupling(channel,"GND")
time.sleep(5)
scoop.setchannelcoupling(channel,"DC")
