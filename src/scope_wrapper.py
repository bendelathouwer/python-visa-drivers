"""wraper for NI-VISA for the oscilloscope """

import sys
import numpy as np
import pyvisa


rm = pyvisa.ResourceManager()
class Scope(object):
    """  reads in the resource string given and try's te establisch coms.
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
        """autoscales the scope """
        self.scope.write(":AUT")

    def clearscope(self):
        """Clear all the waveforms on the screen. """
        self.scope.write(":CLE")

    def scoperun(self):
        """sets the scope in run mode """
        self.scope.write(":RUN")

    def scopestop(self):
        """sets the scope in stop mode """
        self.scope.write(":STOP")

    def singlecapture(self):
        """sets the scope in single capture mode """
        self.scope.write(":SING")

    def forcetrigger(self):
        """forces a trigger and only works in single or normal trigger mode"""
        self.scope.write(":TFOR")

    def querynrofavrages(self):
        """querrys the number of acquisition avarages"""
        avrages=self.scope.query(":ACQ:AVER?")
        return avrages

    def setnrofavrages(self,nr):
        """sets the number of acquisition avarages"""
        self.scope.write(":ACQ:AVER %d"%nr)

    def querymemdepth(self):
        """querrys the number of waveformpoints that can be stored in a single trigger sample
         The default unit is pts (points)"""
        memdepth = self.scope.query(":ACQ:MDEP?")
        return memdepth

    def setmemdepth(self,memmorydepth):
        """sets the number of waveformpoints that can be stored in a single trigger sample
              The default unit is pts (points)"""
        self.scope.write(":ACQ:MDEP %s" % memmorydepth)


    def querraquiretype(self):
        """query the acquisition mode of the oscilloscope"""
        aquiretype = self.scope.query(":ACQ:MDEP?")
        return aquiretype

    def setaquiretype(self, aquiretype):
        """sets the acquisition mode of the oscilloscope"""
        self.scope.write(":ACQuire:TYPE %s" % aquiretype)

    def querysamplerate(self):
        """querrys the samplerate of the scope in samples per second and in engineering notation"""
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
        """query the bandwidth limit parameter of the specified channel."""
        channelbw = self.scope.query(":CHAN%d:BWL?"%channel)
        return channelbw

    def setchannelBW(self,channel,BW):
        """sets channel bandwith of the scope  20MHz"""
        self.scope.write(":CHAN%d:BWL %s " %(channel,BW))

    def querychanelcoupling(self,channel):
        """querry's what channel coupling the  chosen channel has (DC,AC,GND)"""
        channelcoupling = self.scope.query(":CHAN%d:COUP?"%channel)
        return channelcoupling


    def setchannelcoupling(self,channel,coupling):
        """sets what channel coupling the  chosen channel has (DC,AC,GND)"""
        self.scope.write("CHAN%d:COUP %s " %(channel,coupling))

    def querydisplaychannel(self,channel):
        """querry's if the channel is enabled or disabled """
        display = self.scope.query(":CHAN%d:DISP?"%channel)
        return display

    def setdisplaychannel(self,channel,status):
        """enables or disables the """
        self.scope.write("CHAN%d:DISP %s " %(channel,status))

    def querydchannelinversion(self,channel):
        """querry's if the chanel is inverted or not """
        invers = self.scope.query(":CHAN%d:INV?"%channel)
        return invers

    def setchannelinversion(self,channel,inversion):
        """sets the passed channel to inverted """
        self.scope.write("CHAN%d:INV %s " %(channel,inversion))

    def querydchanneloffset(self,channel):#TODO timout opvangen
        offset = self.scope.query(":CHAN%d:OFFS?"%channel)
        return offset

    def querychannelrange(self,channel):#
        range=self.scope.query("CHAN%d:RANG? " %channel)
        return range

    def setchannelrange(self,channel,range):
        self.scope.write("CHAN%d:RANG %s " %(channel,range))

    def querychannelcal(self,channel):#TODO understand this
        cal = self.scope.query("CHAN%d:TCAL? " %channel)
        return cal

    def setchannelcal(self,channel,cal):
        self.scope.write("CHAN%d:TCAL %s " %(channel,cal))

    def querychannelscale(self,channel):#TODO understand this
        scale=self.scope.query("CHAN%d:SCAL? " %channel)
        return scale

    def setchannelscale(self,channel,scale):
        self.scope.write("CHAN%d:SCAL %s " %(channel,scale))

    def querychannelvernier(self,channel):
        status= self.scope.query("CHAN%d:VERN? " % channel)
        return status
    def setchannelvernier(self,channel,vernier):

        self.scope.write("CHAN%d:VERN %s " % (channel, vernier))

    def queryproberatio(self,channel):#TODO understand this
        proberatio=self.scope.query("CHAN%d:PROB? " %channel)
        return proberatio

    def setproberatio(self,channel,ratio):
        self.scope.write("CHAN%d:PROB %s " %(channel,ratio))

    def querychanelunit(self,channel):
        unit = self.scope.query("CHAN%d:UNIT? " % channel)
        return unit

    def setchannelunit(self,channel,unit):
        self.scope.write("CHAN%d:UNIT %s " % (channel, unit))

    def querycursormode(self):
        mode = self.scope.query("CURS:MODE?")
        return mode

    def setcursormode(self,mode):
        self.scope.write("CURS:MODE %s " %mode)

    def querymanualcursortype(self):
        type = self.scope.query("CURS:MAN:TYPE?")
        return type

    def setmanualcursortype(self,cursortype):
        self.scope.write(":CURS:MAN:TYPE %s " %cursortype)

    def querymanualcursorsource(self):
        source = self.scope.query("CURS:MAN:SOUR?")
        return source

    def setmanualcursorsource(self,source):
        self.scope.write("CURS:MAN:SOUR %s " % source)

    def queryycursorunit(self):
        unit = self.scope.query("CURS:MAN:TUN? ")
        return unit

    def setmanualcursorunit(self, unit):
        self.scope.write("CURS:MAN:TUN %s " % unit)

    def queryvertcursorunit(self):
        vertunit = self.scope.query("CURS:MAN:VUN? ")
        return vertunit

    def setmanualvercursorunit(self, vertunit):
        self.scope.write("CURS:MAN:VUN %s " % vertunit)

    def queryemanualAXpos(self):
        AXPOS = self.scope.query("CURS:MAN:AX? ")
        return AXPOS

    def setmanualAXpos(self,axpos):
        self.scope.write("CURS:MAN:AX %s " %axpos)

    def queryemanualbxpos(self):
        bxpos = self.scope.query("CURS:MAN:BX? ")
        return bxpos

    def setmanualAXpos(self,bxpos):
        self.scope.write("CURS:MAN:BX %s " %bxpos)

    def queryemanualaypos(self):
        AYpos = self.scope.query("CURS:MAN:AY? ")
        return AYpos

    def setmanualaypos(self, aypos):
        self.scope.write("CURS:MAN:AY %s " % aypos)

    def queryemanualbypos(self):
        bypos=self.scope.query("CURS:MAN:BY?" )
        return bypos

    def setmanualbypost(self,bypos):
        self.scope.write("CURS:MAN:BY %s"%bypos)

    def querrymanualaxcursorvalue(self):
        cursoraxvalue=self.scope.query("CURS:MANual:AXV?" )
        return cursoraxvalue

    def querrymanualaycursorvalue(self):
        cursorayvalue=self.scope.query("CURS:MAN:AYV? ")
        return cursorayvalue

    def querrymanualbxcursorvalue(self):
        cursorbxvalue = self.scope.query("CURS:MAN:BXV?" )
        return cursorbxvalue

    def querrymanualbycursorvalue(self):
        cursorbyvalue = self.scope.query("CURS:MAN:BYV?")
        return cursorbyvalue

    def querrymanualcursorxdelta(self):
        xdelta= self.scope.query("CURS:MAN:XDEL?")
        return xdelta

    def querrymanualcursorixdelta(self):
        # todo check why it times out when the scpi comand is writen in short
        ixdelta = self.scope.query("CURSor:MANual:IXDELta?")
        return ixdelta

    def querrymanualcursorydelta(self):
        ydelta = self.scope.query("CURS:MAN:YDEL?")
        return ydelta

    def querrytrackcursorsource1(self):
        tracksource1 = self.scope.query("CURS:TRAC:SOUR1? ")
        return tracksource1

    def settraccursorsource1(self,source):
        self.scope.write("CURS:TRAC:SOUR1 %s " % source)

    def querrytrackcursorsource2(self):
        tracksource1 = self.scope.query("CURS:TRAC:SOUR2? ")
        return tracksource1

    def settraccursorsource2(self,source2):
        self.scope.write("CURS:TRAC:SOUR2 %s " % source2)

    def querrycursortrackAX(self):
        axvalue= self.scope.query("CURSor:TRACk:AX? ")
        return axvalue

    def setcursortracAX(self,value):
        self.scope.write("CURSor:TRACk:AX %s " % value)

    def querrycursortrackBX(self):
        bxvalue = self.scope.query("CURSor:TRACk:BX? ")
        return bxvalue

    def setcursortracBX(self, value):
        self.scope.write("CURSor:TRACk:BX %s " % value)


    def querrycursortrackAY(self):
        ayvalue = self.scope.query("CURSor:TRACk:AY? ")
        return ayvalue

    def querrycursortrackBY(self):#need
        byvalue = self.scope.query("CURSor:TRACk:BY? ")
        return byvalue

    def querrycursortrackAXValue(self):
        axvalue = self.scope.query("CURSor:TRACk:AX? ")
        return axvalue

    def querrycursortrackBXValue(self):
        bxvalue = self.scope.query("CURSor:TRACk:BX? ")
        return bxvalue

    def querrycursortrackBYValue(self):
        byvalue = self.scope.query("CURSor:TRACk:BY? ")
        return byvalue


    def querrycursortrackcursorXdelta(self):
        xdeltavalue = self.scope.query("CURSor:TRACk:XDEL? ")
        return xdeltavalue

    def querrycursortrackcursorydelta(self):#needs understanding
        ydeltavalue = self.scope.query("CURSor:TRACk:YDEL? ")
        return ydeltavalue

    def querrycursortrackcursorixdelta(self):#needs understanding
        ixdeltavalue = self.scope.query("CURSor:TRACk:YDEL? ")
        return ixdeltavalue

    def querryautocursornitem(self):
        item = self.scope.query("CURS:AUTO:ITEM? ")
        return item

    def setautocursornitem(self,item):
            self.scope.write("CURS:AUTO:ITEM %s " %item)

    def querryautocursorax(self):
           axvalue = self.scope.query("CURS:AUTO:AX? " )
           return axvalue

    def querryautocursorbx(self):
          bxvalue = self.scope.query("CURS:AUTO:BX? " )
          return bxvalue

    def querryautocursorbx(self):
          bxvalue = self.scope.query("CURS:AUTO:BX? " )
          return bxvalue

    def querryautocursoray(self):
        ayvalue = self.scope.query("CURS:AUTO:ay? " )
        return ayvalue

    def querryautocursorby(self):
        byvalue = self.scope.query("CURS:AUTO:by? " )
        return byvalue

    def querryautocursoraxvalue(self):
        axvalue = self.scope.query("CURS:AUTO:AXV? ")
        return axvalue

    def querryautocursorayvalue(self):
        ayvalue = self.scope.query("CURS:AUTO:AYV? ")
        return ayvalue


    def querryautocursorbxvalue(self):
        bxvalue = self.scope.query("CURS:AUTO:BXV? ")
        return bxvalue

    def querryautocursorbyvalue(self):
        byvalue = self.scope.query("CURS:AUTO:BYV? ")
        return byvalue
    def querryxycursiraxvalue(self):
            axvalue = self.scope.query("CURS:XY:AX? ")
            return axvalue
    def setxycursoraxvalue(self,value):
        self.scope.write("CURS:XY:AX %s" %value)

    def querryxycursirBXvalue(self):
        axvalue = self.scope.query("CURS:XY:BX? ")
        return axvalue

    def setxycursorbxvalue(self, value):
        self.scope.write("CURS:XY:bx %s" % value)

    def querryxycursirayvalue(self):
        axvalue = self.scope.query("CURS:XY:AY? ")
        return axvalue

    def setxycursorayvalue(self, value):
        self.scope.write("CURS:XY:AY %s" % value)

    def querryxycursirbyvalue(self):
        axvalue = self.scope.query("CURS:XY:BY? ")
        return axvalue

    def setxycursorbyalue(self, value):
        self.scope.write("CURS:XY:BY %s" % value)

    def querryxycursorAXalue(self):
        axvalue=self.scope.query("CURS:XY:AX?")
        return axvalue

    def querryxycursorAYalue(self):
        AYvalue = self.scope.query("CURS:XY:AY?")
        return AYvalue

    def querryxycursorBXalue(self):
        axvalue = self.scope.query("CURS:XY:BX?")
        return axvalue
    def querryxycursorBYalue(self):
        AYvalue = self.scope.query("CURS:XY:BY?")
        return AYvalue

    def querrymathdisplay(self):
        display = self.scope.query(":MATH:DISPlay?")
        return display

    def setmathdisplay(self,value):
       self.scope.write(":MATH:DISPlay %s" %value)

    def querrymathopperator(self):
        opperator=self.scope.query(":MATH:OPERator?")
        return opperator

    def setmathopperator (self,opperator):
        self.scope.write(" :MATH:OPERator %s" %opperator)


    def querrymathsource1(self):
        mathsource=self.scope.query(":MATH:SOURce1?")
        return mathsource

    def setmathsource1(self, channel):
        self.scope.write(":MATH:SOURce1 CHANnel%s" %channel)

    def querrymathsource2(self):
        mathsource=self.scope.query(":MATH:SOURce2?")
        return mathsource

    def setmathsource2(self, channel):
        self.scope.write(":MATH:SOURce2 CHANnel%s" %channel)

    def querryLSsource1(self):
        LSsource1=self.scope.query(":MATH:LSOURce1?")
        return LSsource1

    def setLSsource1(self,channel):
        self.scope.query(":MATH:LSOURce1%s" %channel)

    def querryLSsource2(self):
        LSsource2= self.scope.query(":MATH:LSOURce2?")
        return LSsource2

    def setLSsource2(self,channel):
        self.scope.write(":MATH:LSOUrce2 CHAN%s" %channel)

    def querrymathscale(self):
        scale = self.scope.query(":MATH:SCALe?")
        return scale

    def setmathscale(self, scale):
        self.scope.write(":MATH:SCALe %s" % scale)

    def querrymathoffset(self):
        scale = self.scope.query(":MATH:OFFSet? ")
        return scale

    def setmathsoffset(self, scale):
        self.scope.write(" :MATH:OFFSet %s" %scale)




    def querrymathinverd(self):
        """querys the"""
        invert = self.scope.query(":MATH:INVert? ")
        return invert

    def setmathinverd(self, invert):
        self.scope.write(" :MATH:INVert %s" %invert)
    #code from here on out needs to be tested

    def mathreset(self):#needs testing
        self.scope.write(":MATH:RESet")

    def querryFFTsource(self):
        fftsource=self.scope.query(":MATH:FFT:SOURce?")
        return fftsource
    def setFFTsource(self,source):
        self.scope.write(":MATH:FFT:SOURce %s" %source)
    def querryFFTwindow(self):
        fftwindow=self.scope.query(":MATH:FFT:WINDow?")
        return fftwindow
    def setFFTwindow(self,window):
        self.scope.write(":MATH:FFT:WINDow %s" %window)
    def querryFFTsplitwindow(self):
        fftsplitwindow = self.scope.query(":MATH:FFT:SPLit?")
        return fftsplitwindow
    def setFFTsplitwindow(self,split):
        self.scope.write(" :MATH:FFT:SPLit %s" %split)
    def querryFFTunit(self):
       fftunit = self.scope.query("MATH:FFT:UNIT?")
       return fftunit
    def setFFTunit(self,unit):
        self.scope.write(" :MATH:FFT:UNIT %s" %unit)
    def querryFFThorscale(self):
        ffthorschale = self.scope.query(":MATH:FFT:HSCale?")
        return ffthorschale
    def setFFThorscale(self,horscale):
        self.scope.write(":MATH:FFT:HSCale %s" %horscale)

    def querryFFTCenter(self):
        fftcenter = self.scope.query(":MATH:FFT:HCENter?")
        return fftcenter
    def setfftFFTCenter(self,centerFrequency):
        self.scope.write(":MATH:FFT:HCENter %s" %centerFrequency)
    def querryFFTMode(self):
        fftmode=self.scope.query(":MATH:FFT:MODE?")
        return fftmode
    def setFFTMode(self,mode):
        self.scope.write(":MATH:FFT:MODE %s" %mode)

    def querrymathfiltertype(self):
       filtertype = self.scope.query(":MATH:FILTer:TYPE?")
       return filtertype
    def setmathfiltertype(self,filtertype):
        self.scope.write(":MATH:FILTer:TYPE %s" %filtertype)
    def querrymathCutoff1(self):
        cutoff1 = self.scope.query(":MATH:FILTer:W1?")
        return cutoff1
    def setmathcutoff1(self,cutoffFrequency1):
        self.scope.write(":MATH:FILTer:W1 %s" %cutoffFrequency1)
    def querrymathCutoff2(self):
       cutoff2 =  self.scope.query(":MATH:FILTer:W2?")
       return cutoff2
    def setmathcutoff2(self,cutoffFrequency2):
        self.scope.write(":MATH:FILTer:W2 %s" %cutoffFrequency2)
    def querrymathstart(self):
        start = self.scope.query(":MATH:OPTion:STARt?")
        return start
    def setmathstart(self,startpoints):
        self.scope.write(":MATH:OPTion:STARt %s" %startpoints)
    def querrymathend(self):
        end = self.scope.query(":MATH:OPTion:END?")
        return end
    def setmathstart(self,endpoints):
        self.scope.write(":MATH:OPTion:END %s" %endpoints)
    def querrymathinvert(self):
        invert = self.scope.query(":MATH:OPTion:INVert?")
        return invert
    def setmathinvert(self,setinvert):
        self.scope.write("::MATH:OPTion:INVert %s" %setinvert)
    def querrymathopionsens(self):
        sensoptions = self.scope.query(":MATH:OPTion:SENSitivity?")
        return sensoptions
    def setmathoptionsens(self,senstivity): # find a way to check if the step of 0.8 is  ok
        if senstivity>0.96:#if sensitivity is higer then 0.96 snap to 0,96
            senstivity=0.96
        self.scope.write(":MATH:OPTion:SENSitivity %s" %senstivity)
    def querrymathdistance(self):
        distance = self.scope.query(":MATH:OPTion:DIStance?")
        return distance

    def setotpiondistance (self,distance):
        if distance >201:  # if sensitivity is higer then 0.96 snap to 0,96
            distance = 201
        if distance < 3:
            distance =3
        self.scope.write(":MATH:OPTion:DIStance? %s" % distance)
    def querrymathautoscale(self):
        mathautoschale=self.scope.query(":MATH:OPTion:ASCale?")
        return mathautoschale
    def setmathautoscale(self,autoscale):
        self.scope.write(":MATH:OPTion:ASCale? %s" % autoscale)
    def querrymathlogictreshold1(self):
        logictreshhold1 = self.scope.query(":MATH:OPTion:THReshold1?")
        return logictreshhold1
    def setmathlogichtreshold1(self,logictreshold1):
        self.scope.write(" :MATH:OPTion:THReshold1 %s" %logictreshold1)
    def querrymathlogictreshold2(self):
        logictreshhold2 = self.scope.query(":MATH:OPTion:THReshold2?")
        return logictreshhold2
    def setmathlogichtreshold2(self,logictreshold2):
        self.scope.write(" :MATH:OPTion:THReshold2 %s" %logictreshold2)
    def querrymathfxsource1(self):
        mathfxsource1 = self.scope.query(":MATH:OPTion:FX:SOURce1?")
        return mathfxsource1
    def setmathfxsource1(self,fxsource1):
        self.scope.write("MATH:OPTion:FX:SOURce1 %s" %fxsource1)

    def querrymathfxsource2(self):
        mathfxsource2 = self.scope.query(":MATH:OPTion:FX:SOURce2?")
        return mathfxsource2

    def setmathfxsource1(self, fxsource2):
        self.scope.write("MATH:OPTion:FX:SOURce2 %s" % fxsource2)

    def querymathfxoperator(self):
        mathfxoperator = self.scope.query(":MATH:OPTion:FX:OPERator?")
        return mathfxoperator
    def setmathfxoperator(self,fxoperator):
        self.scope.write(":MATH:OPTion:FX:OPERator%s" %fxoperator)
    def querrymaskenable(self):
        maskenabled = self.scope.query(":MASK:ENABle?")
        return maskenabled
    def setmaskeenable(self,maskenabled):
        self.scope.write(":MASK:ENABle %s" %maskenabled)

    def querrymasksource(self):
        masksource = self.scope.query(":MASK:SOURce?")
        return masksource

    def setmasksource (self,masksource):
        self.scope.write(" :MASK:SOURce %s" %masksource)

    def querrymaskoperating(self):
        maskoperating = self.scope.query(":MASK:OPERate?")
        return maskoperating

    def setmaskoperating(self, maskoperating):
        self.scope.write(":MASK:OPERate %s" %maskoperating)

    def querrymaskstats(self):
        maskstats = self.scope.query(":MASK:MDISplay?")
        return maskstats

    def setmaskstats(self,maskstats):
        self.scope.write(":MASK:MDISpl %s"%maskstats)

    def querrymaskstoponfail(self):
        stoponfail = self.scope.query(":MASK:SOOutput?")
        return stoponfail

    def setmaskstoponfail(self,stoponfail):
        self.scope.write(":MASK:SOOutput %s" %stoponfail)

    def querrymaskoutput(self):
        maskoutput = self.scope.query(":MASK:OUTPut?")
        return maskoutput

    def setmaskoutput(self,maskoutput):
        self.scope.write(":MASK:OUTPut %s"%maskoutput)

    def querrymaskx(self):
        maskx = self.scope.query(":MASK:X?")
        return maskx

    def setmaskx(self,maskx):
        if maskx<0.02:
            maskx=0.02
        if maskx>4:
            maskx=4
        self.scope.write(":MASK:X %s" %maskx)

    def querrymasky(self):
        masky = self.scope.query(":MASK:Y?")
        return masky

    def setmaskx(self, masky):
        if masky < 0.04:
            masky = 0.04
        if masky > 5.12:
            masky = 5.12
        self.scope.write(":MASK:Y %s" % masky)

    def setcreatemask(self):
        self.scope.write(":MASK:CREate")

    def querrymaskpased(self):
        maskepassed = self.scope.query(":MASK:PASSed?")
        return maskepassed

    def querrymaskfailed(self):
        maskefailed = self.scope.query(":MASK:FAILed??")
        return maskefailed

    def querrymasktotal(self):
        masktotal = self.scope.query(":MASK:TOTal?")
        return masktotal

    def setmaskreset(self):
        self.scope.write(":MASK:RESet")

    def querrymeasurmentsource(self):
        measurmentsource = self.scope.query(":MEASure:SOURce?")
        return measurmentsource

    def setmeasurmentsource(self,measurmentsource):
        self.scope.write(":MEASure:SOURce %s" % measurmentsource)

    def querrymeasurmentsource(self):
        measurmentcountersource = self.scope.query(":MEASure:COUNter:SOURce?")
        return measurmentcountersource

    def setmeasurmentsource(self,measurmentcountersource):
        self.scope.write(":MEASure:COUNter:SOURce  %s" % measurmentcountersource)

    def querrymeasurmentcountervalue(self):
        countervalue = self.scope.query(":MEASure:COUNter:VALue?")
        if countervalue == 0:
            return "counter not enabbled" # need other divices to test this
        return countervalue + "Hz"

    def setmeasurementclear(self,clearitem):
        self.scope.write(":MEASure:CLEar %s" % clearitem)

    def setmeasurementrecover(self,recoveritem):
        self.scope.write(":MEASure:RECover %s" % recoveritem)

    def querrymeasureall(self):
        allmeasurmentenabled = self.scope.query(":MEASure:ADISplay?")
        return allmeasurmentenabled

    def setmeasurmentall(self,enable):
        self.scope.write(":MEASure:ADISplay %s" % enable)

    def querrymesurmentallsource(self):
        measurmentallsource = self.scope.query(":MEASure:AMSource?")
        return measurmentallsource

    #test multipe inputs and try to catch them aka make it work
    def setmeasurmentallsource(self,source):
        self.scope.write("MEASure:AMSource %s" %source)

    def querrymeasuremax(self):
        setupmax = self.scope.query(":MEASure:SETup:MAX?")
        return setupmax

    def setmeasurmentmax(self,setupmax ):
        if setupmax <7:
            setupmax == 7
        if setupmax>95:
            setupmax == 95
        self.scope.write(":MEASure:SETup:MAX %s"%setupmax)

    def querrymeasuremid(self):
        setupmid= self.scope.query(":MEASure:SETup:MID?")
        return setupmid

    def setmeasurmentmid(self, setupmid):
        if setupmid < 6:
            setupmid == 5
        if setupmid > 94:
            setupmid == 94
        self.scope.write(":MEASure:SETup:MID %s" % setupmid)

    def querrymeasuremin(self):
        setupmin = self.scope.query(":MEASure:SETup:MIN?")
        return setupmin

    def setmeasurmentmin(self, setupmin):
        if setupmin < 5:
            setupmin == 5
        if setupmin > 93:
            setupmin == 93
        self.scope.write(":MEASure:SETup:MIN %s" % setupmin)
    def querryphasemeasurmentsourcea(self):
        phasesoursea = self.scope.query(":MEASure:SETup:PSA?")
        return phasesoursea
    def setphasemeasurmentsourcea(self,phasesourcea):
        self.scope.write(":MEASure:SETup:PSA %" %phasesourcea)

    def querryphasemeasurmentsourceb(self):
        phasesoursea = self.scope.query(":MEASure:SETup:PSB?")
        return phasesoursea

    def setphasemeasurmentsourceb(self, phasesourceb):
        self.scope.write(":MEASure:SETup:PSB %s" % phasesourceb)

    def querrymeasurmentdelaysourcea(self):
        delaysourcea = self.scope.query(":MEASure:SETup:DSA?")
        return delaysourcea
    def setmeasurmentdelaysourcea(self,delaysourcea):
        self.scope.write(":MEASure:SETup:DSA %" %delaysourcea)

    def querrymeasurmentdelaysourceb(self):
        delaysourceb = self.scope.query(":MEASure:SETup:DSB?")
        return delaysourceb

    def setmeasurmentdelaysourceb(self, delaysourceb):
        self.scope.write(":MEASure:SETup:DSB %" % delaysourceb)

    def querrymeasurmentstatdisplay(self):
        statusdisplay = self.scope.query(":MEASure:STATistic:DISPlay?")
        return statusdisplay

    def setmeasurmentstatdesplay(self,statusdisplay):
        self.scope.write(":MEASure:STATistic:DISPlay %" %statusdisplay)

    def querrymeasurmentstatmode(self):
        statmode = self.scope.query(":MEASure:STATistic:MODE? ")
        return statmode

    def setmeasurmentstatmode(self,statmode):
        self.scope.write(":MEASure:STATistic:MODE %" %statmode)

    def measurmentstatreset(self):
        self.scope.write(":MEASure:STATistic:RESet")

    def takemeasurement(self,channel,mode,form):
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





