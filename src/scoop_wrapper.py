import pyvisa
def scoopinit (scoop_adder):
    rm = pyvisa.ResourceManager()
    scoop = rm.open_resource(scoop_adder)
    print(scoop.query("*IDN?"))
