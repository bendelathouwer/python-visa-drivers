"""wraper for NI-VISA for the oscilloscope """

import sys
import numpy as np
import pyvisa


rm = pyvisa.ResourceManager()
class Scope(object):
    """ Reads in the resource string given and try's te establisch coms.
    Also prints the connecte identifyer string """
    def __init__(self,visaadder):
        self.visa_instr_list= rm.list_resources()
        self.scope = rm.open_resource(visaadder)
        idn_string = self.scope.query("*IDN?")
        if len(idn_string) == 0:
            print("ERROR: no instrument found!")
            print("Exited because of error.")
            sys.exit(1)
        else:
            print("Identification string: %s" % idn_string)
        self.scope.timeout = 20000

    def autoscale(self):
        """Autoscales the scope """
        self.scope.write(":AUT")

    def clearscope(self):
        """Clear all the waveforms on the screen. """
        self.scope.write(":CLE")

    def scoperun(self):
        """Sets the scope in run mode """
        self.scope.write(":RUN")

    def scopestop(self):
        """Sets the scope in stop mode """
        self.scope.write(":STOP")

    def singlecapture(self):
        """Sets the scope in single capture mode """
        self.scope.write(":SING")

    def forcetrigger(self):
        """forces a trigger and only works in single or normal trigger mode"""
        self.scope.write(":TFOR")

    def querynrofavrages(self):
        """Querry's the number of acquisition avarages"""
        avrages=self.scope.query(":ACQ:AVER?")
        return avrages

    def setnrofavrages(self,nr):
        """Sets the number of acquisition avarages"""
        self.scope.write(":ACQ:AVER %d"%nr)

    def querymemdepth(self):
        """Querry's the number of waveformpoints that can be stored in a single trigger sample
         The default unit is pts (points)"""
        memdepth = self.scope.query(":ACQ:MDEP?")
        return memdepth

    def setmemdepth(self,memmorydepth):
        """Sets the number of waveformpoints that can be stored in a single trigger sample
              The default unit is pts (points)"""
        self.scope.write(":ACQ:MDEP %s" % memmorydepth)


    def querraquiretype(self):
        """Querry's the acquisition mode of the oscilloscope"""
        aquiretype = self.scope.query(":ACQ:MDEP?")
        return aquiretype

    def setaquiretype(self, aquiretype):
        """Sets the acquisition mode of the oscilloscope"""
        self.scope.write(":ACQuire:TYPE %s" % aquiretype)

    def querysamplerate(self):
        """Querry's the samplerate of the scope in samples per second and in engineering notation"""
        samplerate = self.scope.query(":ACQ:SRAT?")
        return samplerate

    def startcal(self):
        """ starts the automatic callibration of the scope """
        print("DISCONECT EVERYTHING!")
        self.scope.timeout(5000)
        self.scope.write(":CAL:STAR")

    def stopcal(self):
        """ stops the automatic callibration of the scope """
        self.scope.write(":CAL:QUIT")

    def querychanelBW(self,channel):
        """Querry's the bandwidth limit parameter of the specified channel."""
        channelbw = self.scope.query(":CHAN%d:BWL?"%channel)
        return channelbw

    def setchannelBW(self,channel,BW):
        """Sets channel bandwith of the scope  20MHz"""
        self.scope.write(":CHAN%d:BWL %s " %(channel,BW))

    def querychanelcoupling(self,channel):
        """Querry's what channel coupling the  chosen channel has (DC,AC,GND)"""
        channelcoupling = self.scope.query(":CHAN%d:COUP?"%channel)
        return channelcoupling


    def setchannelcoupling(self,channel,coupling):
        """Sets what channel coupling the  chosen channel has (DC,AC,GND)"""
        self.scope.write("CHAN%d:COUP %s " %(channel,coupling))

    def querydisplaychannel(self,channel):
        """Querry's if the channel is enabled or disabled """
        display = self.scope.query(":CHAN%d:DISP?"%channel)
        return display

    def setdisplaychannel(self,channel,status):
        """Sets if the channel is enabled or disabled """
        self.scope.write("CHAN%d:DISP %s " %(channel,status))

    def querydchannelinversion(self,channel):
        """Querry's if the chanel is inverted or not """
        invers = self.scope.query(":CHAN%d:INV?"%channel)
        return invers

    def setchannelinversion(self,channel,inversion):
        """Sets the passed channel to inverted """
        self.scope.write("CHAN%d:INV %s " %(channel,inversion))

    def querydchanneloffset(self,channel):
        """Querrys the channel ofset , returnd in volts and engineering notation """
        offset = self.scope.query(":CHAN%d:OFFS?"%channel)
        return offset

    def setdchanneloffset(self,channel,offset):
        """Sets the offset of the specified channel using volts and in engineering notation"""
        self.scope.query(":CHAN %s:OFFS %s"%(channel,offset))


    def querychannelrange(self,channel):
        """Querry's the vertical range of the instrument , unit used is volts """
        range=self.scope.query("CHAN%d:RANG? " %channel)
        return range

    def setchannelrange(self,channel,range):
        """sets the range of the specified channel, nit is volts and using engineering notation  """
        self.scope.write("CHAN%d:RANG %s " %(channel,range))

    def querychannelcal(self,channel):
        """  Set the delay calibration time of the specified channel to calibrate the zero offset ,unit is s and using engineering notation"""
        cal = self.scope.query("CHAN%d:TCAL? " %channel)
        return cal

    def setchannelcal(self,channel,cal):
        """Set the delay calibration time of the specified channel to calibrate the zero offset
           of the corresponding channel. Unit is s and using engineering notation """
        self.scope.write("CHAN%d:TCAL %s " %(channel,cal))

    def querychannelscale(self,channel):
        """Query the vertical scale of the specified channel. The default unit is V and uses engineering notation.
        this is also dependend on the probe attenuation"""
        scale=self.scope.query("CHAN%d:SCAL? " %channel)
        return scale

    def setchannelscale(self,channel,scale):
        """Sets the vertical scale of the specified channel. The default unit is V and uses engineering notation.
        this is also dependend on the probe attenuation
        """
        self.scope.write("CHAN%d:SCAL %s " %(channel,scale))


    def queryproberatio(self,channel):
        """Querry's the probe ratio.Default value is 10x . This is the attenuation of speccified channel.
        Using the following attenuations 0.01|0.02|0.05|0.1|0.2|0.5|1|2|5|10|20|50|
        100|200|500|1000"""
        proberatio=self.scope.query("CHAN%d:PROB? " %channel)
        return proberatio

    def setproberatio(self,channel,ratio):
        """Sets the probe ratio.Default value is 10x . This is the attenuation of speccified channel.
        Using the following attenuations 0.01|0.02|0.05|0.1|0.2|0.5|1|2|5|10|20|50|
        100|200|500|1000"""
        self.scope.write("CHAN%d:PROB %s " %(channel,ratio))

    def querychanelunit(self,channel):
        """Querry's the channel unit of the specified channel. The following parameters can be returned
        VOLTage|WATT|AMPere|UNKNown. Default value is VOLTage"""
        unit = self.scope.query("CHAN%d:UNIT? " % channel)
        return unit

    def setchannelunit(self,channel,unit):
        """Querry's the channel unit of the specified channel. The following parameters can be passed
               VOLTage|WATT|AMPere|UNKNown. Default value is VOLTage"""
        self.scope.write("CHAN%d:UNIT %s " % (channel, unit))

    def querrychannelvernier(self,channel):
        """Querry's the vernier status of the speccified channel. The default state is of"""
        vernier=self.scope.write("CHAN%d:VERN ?" % (channel))
        return vernier

    def setchannelvernier(self,channel,vernier):
        """ Sets the vernier status of the speccified channel. """
        self.scope.write("CHAN%d:VERN %s " % (channel, vernier))


    def querycursormode(self):
        """Querry's the cursor measurement mode. Returns one of the following params OFF|MANual|TRACk|AUTO|XY.
         The default param is OFF"""
        mode = self.scope.query("CURS:MODE?")
        return mode

    def setcursormode(self,mode):
        """Sets the cursor measurement mode. Returns one of the following params OFF|MANual|TRACk|AUTO|XY.
               The default param is OFF, XY only works when the horizontal timebase mode is in XY"""
        self.scope.write("CURS:MODE %s " %mode)

    def querymanualcursortype(self):
        """Querry's  the cursor type in manual cursor measurement mode. Returns the folowing params X|Y,
        default param is x"""

        type = self.scope.query("CURS:MAN:TYPE?")
        return type

    def setmanualcursortype(self,cursortype):
        """Sets the cursor type in manual cursor measurement mode. Returns the folowing params X|Y,
              default param is x"""
        self.scope.write(":CURS:MAN:TYPE %s " %cursortype)


    def querymanualcursorsource(self):
        """Querry's the source of the manual cursors, returns one of the 
        following params {CHANnel1|CHANnel2|CHANnel3|CHANnel4|MATH|LA"""
        source = self.scope.query("CURS:MAN:SOUR?")
        return source

    def setmanualcursorsource(self,source):
        """sets's the source of the manual cursors, returns one of the 
        following params {CHANnel1|CHANnel2|CHANnel3|CHANnel4|MATH|LA"""
        self.scope.write("CURS:MAN:SOUR %s " % source)

    def queryycursorunit(self):
        """
        querry's the cursor unit , returns S|HZ|DEGRee|PERCent
        """
        unit = self.scope.query("CURS:MAN:TUN? ")
        return unit

    def setmanualcursorunit(self, unit):
        """ sets the cursor unit , returns S|HZ|DEGRee|PERCent"""
        self.scope.write("CURS:MAN:TUN %s " % unit)

    def queryvertcursorunit(self):
        """querry's the vertical curserunit , returns percent or source. 
        The latter uses the unit from the source """
        vertunit = self.scope.query("CURS:MAN:VUN? ")
        return vertunit

    def setmanualvercursorunit(self, vertunit):
        """sets the vertical unit , this can be PERCent for 
        percentage or SOURce for the unit wich is curently 
        in use by the source """
        self.scope.write("CURS:MAN:VUN %s " % vertunit)

    def queryemanualAXpos(self):
        """querys the manual cursor position 
        of the horizontal a cursor, range 5-594, default 100
        """
        AXPOS = self.scope.query("CURS:MAN:AX? ")
        return AXPOS

    def setmanualAXpos(self,axpos):
        """querys the manual cursor position 
        of the horizontal a cursor ,range 5-594 default 100
       TODO add range controll to catch out of bounds """
        self.scope.write("CURS:MAN:AX %s " %axpos)

    def queryemanualbxpos(self):
        """querry's the horizontal b cursor in manual mode
        range is from 5 to 594"""
        bxpos = self.scope.query("CURS:MAN:BX? ")
        return bxpos

    def takemeasurement(self,channel,mode,form):
        
        """Reads the data  from the speccified channel , and in the specified mode and format
        mode:
        NORMal: read the waveform data displayed on the screen.   
        MAXimum: read the waveform data displayed on the screen when the instrument is in the run state and the waveform data in the internal memory in the stop state. 
        RAW: read the waveform data in the internal memory. Note that the waveform data in the internal memory can only be read when the oscilloscope is in the stop state and the oscilloscope cannot be operated during the reading process.
        format:
        WORD: a waveform point occupies two bytes (namely 16 bits) in which the lower 8 bits are valid and the higher 8 bits are 0.   
        BYTE: a waveform point occupies one byte (namely 8 bits). 
        ASCii: return the actual voltage value of each waveform point in scientific notation. The voltage values are separated by commas. """
        self.scope.write(":WAVeform:SOURce %s" %channel)
        self.scope.write(":WAVeform:MODE %s" %mode)
        self.scope.write( ":WAVeform:FORMat %s " % form)
        waveformdata = []
        waveformdata = self.scope.query(":WAVeform:DATA?")

        # removes the first element (the first 11 caracters)
        # it's  not part of the data
        # parses string to a 1d  numpy array separates on a given seperator
        newwaveformdata = np.fromstring(waveformdata[11:], sep=",")
        return newwaveformdata





