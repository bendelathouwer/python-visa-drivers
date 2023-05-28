import scoop_wrapper
import time
scoop=scoop_wrapper.scoop("TCPIP0::169.254.226.8::INSTR")
channel=4
scoop.setdisplaychannel(channel,1)
time.sleep(5)
scoop.setdisplaychannel(channel,0)
time.sleep(5)
scoop.setdisplaychannel(channel,"ON")
time.sleep(5)
scoop.setdisplaychannel(channel,"OFF")