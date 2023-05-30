import scoop_wrapper
import time
scoop=scoop_wrapper.scoop("TCPIP0::169.254.226.8::INSTR")
channel=2
scoop.setchanneloffset(channel,0)
