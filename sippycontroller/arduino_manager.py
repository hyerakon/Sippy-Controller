from nanpy  import ArduinoApi, SerialManager
import time

#include <SimpleTimer.h>


#INPUT
#  A8  - SensoreLuce
#  A9  - SensoreTemperaturaAcqua
#  A10 - SensorePH
#  A11 - SensoreLivelloAcqua
#  A12 - SensoreEC
#  A13 - NotConnected
#
#OUTPUT - per accendere o spegnere moduli
#5v:
#  D28 - PH
#  D29 - LivelloAcqua
#  D26 - EC
#  D27 - NotConnected
#12v:
#  D24 - Piezo
#  D25 - PompaAcqua
#  D22 - PompaAria
#  D23 - Luci
#
#6.0 to 6.5: Ideal pH Level
#650 to 750 PPM


SensoreLuce =8
SensoreTemp =9
SensorePh =10
SensoreAcqua =11
SensoreTds =12
#define  A13

AlimentazionePh =28
AlimentazioneLivelloAcqua =29
AlimentazioneTds =26
#define NotConnected 27
AlimentazionePiezo =24
AlimentazionePompaAcqua =25
AlimentazionePompaAria =22
AlimentazioneLuci =23

#valori
tds = 0
ph = 0
luce = 0
acqua = 0
temp = 0

VREF =5.0      # analog reference voltage(Volt) of the ADC
SCOUNT  =30

#per Luce
analogBufferLuce=[SCOUNT]    # store the analog value in the array, read from ADC
analogBufferTempLuce=[SCOUNT] 
analogBufferIndexLuce = 0
copyIndexLuce = 0
averageVoltageLuce = 0





############# SETUP ARDUINO
def arduino_setup():
    print('ARDUINO CONNECTION!')

    connection = SerialManager(device='COM3')
    arduino = ArduinoApi(connection=connection)

    arduino.pinMode(AlimentazionePh,arduino.OUTPUT)
    arduino.pinMode(AlimentazioneLivelloAcqua,arduino.OUTPUT)
    arduino.pinMode(AlimentazioneTds,arduino.OUTPUT)
    arduino.pinMode(AlimentazionePiezo,arduino.OUTPUT)
    arduino.pinMode(AlimentazionePompaAcqua,arduino.OUTPUT)
    arduino.pinMode(AlimentazionePompaAria,arduino.OUTPUT)
    arduino.pinMode(AlimentazioneLuci,arduino.OUTPUT)

    arduino.pinMode(SensoreLuce,arduino.INPUT)
    arduino.pinMode(SensoreTemp,arduino.INPUT)
    arduino.pinMode(SensorePh,arduino.INPUT)
    arduino.pinMode(SensoreAcqua,arduino.INPUT)
    arduino.pinMode(SensoreTds,arduino.INPUT)
    arduino.digitalWrite(AlimentazionePompaAria, arduino.HIGH)


############# LOOP ARDUINO




def _test():
    print ("Start: Arduino Manager")

if __name__ == "__main__":
    _test()
