import pyvisa
import sys
rm = pyvisa.ResourceManager()
class scoop(object):
    # TODO: error handeling beter op poten zetten
    def __init__(self):
        self.visaInstrList= rm.list_resources()
        print(self.visaInstrList)
        if len(self.visaInstrList) == 0:
            print("ERROR: no instrument found!")
            print("Exited because of error.")
            sys.exit(1)
        myscope = self.visaInstrList[0]
        self.scope = rm.open_resource(myscope)
        idn_string = self.scope.query("*IDN?")
        if len(idn_string) == 0:
            print("ERROR: no instrument found!")
            print("Exited because of error.")
            sys.exit(1)
        else:
            print("Identification string: '%s'" % idn_string)
        self.scope.timeout = 15000
    def setchannels(self,channelnr,channelstatus):
        pass