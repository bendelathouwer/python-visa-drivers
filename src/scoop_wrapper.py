import pyvisa
import sys
import time
rm = pyvisa.ResourceManager()
class scoop(object):
    # TODO: error handeling beter op poten zetten+ visa instument list "variable maken
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
    def autoscale(self):#autoscales the scoop trace on any channel
        self.scope.write(":AUT")
    def clearscoop(self):#clears the traces in single run mode from the display
        self.scope.write(":CLE")
    def scooprun(self):#sets the scope  in run mode
        self.scope.write(":RUN")
    def scoopstop(self):#sets the scope  in stop mode
        self.scope.write(":STOP")
    def singlecapture(self):
        self.scope.write(":SING")
    def forcetrigger(self):#only works in single or normal trigger mode
        self.scope.write(":TFOR")
    def nrofavrages(self):
        nr=self.scope.query(":ACQ:AVER?")
        return nr
    def setnrofavrages(self,nr):#error 

        self.scope.write(":ACQ:AVER"+str(nr))
