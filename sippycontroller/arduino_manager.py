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
acqua = 2000
temp = 0

VREF =5.0      # analog reference voltage(Volt) of the ADC
SCOUNT  =30

# per TDS
analogBufferTds=[SCOUNT]    # store the analog value in the array, read from ADC
analogBufferTempTds=[SCOUNT]
analogBufferIndexTds = 0
copyIndexTds = 0
averageVoltageTds = 0.0

# per PH
calibration_value = 21.34 - 0.1
analogBufferPh=[SCOUNT]    # store the analog value in the array, read from ADC
analogBufferTempPh=[SCOUNT]
analogBufferIndexPh = 0
copyIndexPh = 0
averageVoltagePh = 0.0

# per Acqua
analogBufferAcqua=[SCOUNT]    #store the analog value in the array, read from ADC
analogBufferTempAcqua=[SCOUNT]
analogBufferIndexAcqua = 0
copyIndexAcqua = 0
averageVoltageAcqua = 0.0

# per Luce
analogBufferLuce=[SCOUNT]    # store the analog value in the array, read from ADC
analogBufferTempLuce=[SCOUNT] 
analogBufferIndexLuce = 0
copyIndexLuce = 0
averageVoltageLuce = 0

# per Temp
analogBufferTemp=[SCOUNT];    #store the analog value in the array, read from ADC
analogBufferTempTemp=[SCOUNT]
analogBufferIndexTemp = 0
copyIndexTemp = 0

averageVoltageTemp = 0.0
R1 = 10000.0
logR2 = 0.0
R2 = 0.0
T = 0.0
Tc = 0.0
Tf = 0.0
c1 = 1.009249522e-03
c2 = 2.378405444e-04
c3 = 2.019202697e-07



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
def arduino_loop(arduino, connection):

    #StartReadTdsSensor
    arduino.digitalWrite(AlimentazioneTds, arduino.HIGH)
    arduino.delay(10)
    
    analogSampleTimepointTds = arduino.millis()

    if (arduino.millis()-analogSampleTimepointTds) > 50U : #every 40 milliseconds,read the analog value from the ADC
        arduino.analogSampleTimepointTds = arduino.millis()
        analogBufferTds[analogBufferIndexTds] = arduino.analogRead(SensoreTds);    #read the analog value and store into the buffer
        analogBufferIndexTds+1
        if analogBufferIndexTds == SCOUNT: 
            analogBufferIndexTds = 0
    
    
    arduino.digitalWrite(AlimentazioneTds, arduino.LOW)
    
    
    printTimepointTds = arduino.millis()
    if (arduino.millis()-printTimepointTds) > 1500U:
        printTimepointTds = arduino.millis()
        
        for copyIndexTds in range(0,SCOUNT):
            analogBufferTempTds[copyIndexTds]= analogBufferTds[copyIndexTds]
        averageVoltageTds = getMedianNum(analogBufferTempTds,SCOUNT) * VREF / 1024.0; # read the analog value more stable by the median filtering algorithm, and convert to voltage value
        
        compensationCoefficient=1.0+0.02*(temp-25.0)    #temperature compensation formula: fFinalResult(25^C) = fFinalResult(current)/(1.0+0.02*(fTP-25.0));
        compensationVolatge=averageVoltageTds/compensationCoefficient;  #temperature compensation
        tds=(133.42*compensationVolatge*compensationVolatge*compensationVolatge - 255.86*compensationVolatge*compensationVolatge + 857.39*compensationVolatge)*0.5; #convert voltage value to tds value
    
    #EndReadTdsSensor

    //StartReadPhSensor
    digitalWrite(AlimentazionePh, HIGH);
    //delay(20);

    static unsigned long analogSampleTimepointPh = millis();
    if(millis()-analogSampleTimepointPh > 50U) {    //every 40 milliseconds,read the analog value from the ADC
        analogSampleTimepointPh = millis();
        analogBufferPh[analogBufferIndexPh] = analogRead(SensorePh);    //read the analog value and store into the buffer
        analogBufferIndexPh++;
        if(analogBufferIndexPh == SCOUNT) 
            analogBufferIndexPh = 0;
    }
    
    digitalWrite(AlimentazionePh, LOW);

    static unsigned long printTimepointPh = millis();
    if(millis()-printTimepointPh > 1500U) {
        printTimepointPh = millis();
        for(copyIndexPh=0;copyIndexPh<SCOUNT;copyIndexPh++)
            analogBufferTempPh[copyIndexPh]= analogBufferPh[copyIndexPh];
        averageVoltagePh = getMedianNum(analogBufferTempPh,SCOUNT) * (float)VREF / 1024.0; // read the analog value more stable by the median filtering algorithm, and convert to voltage value
        ph = -5.70 * averageVoltagePh + calibration_value;    
    } 
    //EndReadPhSensor

    //StartReadWaterSensor
    digitalWrite(AlimentazioneLivelloAcqua, HIGH);
    //delay(20);

    static unsigned long analogSampleTimepointAcqua = millis();
    if(millis()-analogSampleTimepointAcqua > 50U) {    //every 40 milliseconds,read the analog value from the ADC
        analogSampleTimepointAcqua = millis();
        analogBufferAcqua[analogBufferIndexAcqua] = analogRead(SensoreAcqua);    //read the analog value and store into the buffer
        analogBufferIndexAcqua++;
        if(analogBufferIndexAcqua == SCOUNT) 
            analogBufferIndexAcqua = 0;
    }
    
    digitalWrite(AlimentazioneLivelloAcqua, LOW);

    static unsigned long printTimepointAcqua = millis();
    if(millis()-printTimepointAcqua > 1500U) {
        printTimepointAcqua = millis();
        for(copyIndexAcqua=0;copyIndexAcqua<SCOUNT;copyIndexAcqua++)
            analogBufferTempAcqua[copyIndexAcqua]= analogBufferAcqua[copyIndexAcqua];
        averageVoltageAcqua = getMedianNum(analogBufferTempAcqua,SCOUNT) * (float)VREF / 1024.0; // read the analog value more stable by the median filtering algorithm, and convert to voltage value
        acqua = averageVoltageAcqua/VREF; //non mi importa di quanta acqua ci sia realmente, basta ci sia
    } 

    if(acqua > 0.1)
        digitalWrite(AlimentazionePompaAcqua, HIGH);
    else
        digitalWrite(AlimentazionePompaAcqua, LOW);    
    //EndReadWaterSensor

    //StartReadLightSensor
    static unsigned long analogSampleTimepointLuce = millis();
    if(millis()-analogSampleTimepointLuce > 50U) {    //every 40 milliseconds,read the analog value from the ADC
        analogSampleTimepointLuce = millis();
        analogBufferLuce[analogBufferIndexLuce] = analogRead(SensoreLuce);    //read the analog value and store into the buffer
        analogBufferIndexLuce++;
        if(analogBufferIndexLuce == SCOUNT) 
            analogBufferIndexLuce = 0;
    }

    static unsigned long printTimepointLuce = millis();
    if(millis()-printTimepointLuce > 1500U) {
        printTimepointLuce = millis();
        for(copyIndexLuce=0;copyIndexLuce<SCOUNT;copyIndexLuce++)
            analogBufferTempLuce[copyIndexLuce]= analogBufferLuce[copyIndexLuce];
        averageVoltageLuce = getMedianNum(analogBufferTempLuce,SCOUNT) * (float)VREF / 1024.0; // read the analog value more stable by the median filtering algorithm, and convert to voltage value
        luce = averageVoltageLuce/VREF; //non mi importa di quanta luce ci sia realmente, basta ci sia
    }

    if(luce < 0.5)
        digitalWrite(AlimentazioneLuci, HIGH);
    else
        digitalWrite(AlimentazioneLuci, LOW);
    //EndReadLightSensor

    //StartReadTempSensor
    static unsigned long analogSampleTimepointTemp = millis();
    if(millis()-analogSampleTimepointTemp > 50U) {    //every 40 milliseconds,read the analog value from the ADC
        analogSampleTimepointTemp = millis();
        analogBufferTemp[analogBufferIndexTemp] = analogRead(SensoreTemp);    //read the analog value and store into the buffer
        analogBufferIndexTemp++;
        if(analogBufferIndexTemp == SCOUNT) 
            analogBufferIndexTemp = 0;
    }

    static unsigned long printTimepointTemp = millis();
    if(millis()-printTimepointTemp > 1500U) {
        printTimepointTemp = millis();
        for(copyIndexTemp=0;copyIndexTemp<SCOUNT;copyIndexTemp++)
            analogBufferTempTemp[copyIndexTemp]= analogBufferTemp[copyIndexTemp];
        averageVoltageTemp = getMedianNum(analogBufferTempTemp,SCOUNT); // read the analog value more stable by the median filtering algorithm, and convert to voltage value
        R2 = R1 * (1023.0 / (float)averageVoltageTemp - 1.0);
        logR2 = log(R2);
        T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2));
        temp = T - 273.15;
    }

    if(temp < 18)
        digitalWrite(AlimentazionePiezo, HIGH);
    else
        digitalWrite(AlimentazionePiezo, LOW);
    //EndReadTempSensor
    
    static unsigned long printAll = millis();
    if(millis()-printAll > 1000U) {
        printAll = millis();
        stampaValori();
    }

def getMedianNum(bArray, iFilterLen):
    bTab=[iFilterLen]
      
    for i in range(0,iFilterLen):
        bTab[i] = bArray[i]
      
    bTemp=0

    for j in range(0,iFilterLen):
        for i in range(0,iFilterLen):
            if bTab[i] > bTab[i + 1]:
                bTemp = bTab[i]
                bTab[i] = bTab[i + 1]
                bTab[i + 1] = bTemp
        

      if ((iFilterLen & 1) > 0)
    bTemp = bTab[(iFilterLen - 1) / 2];
      else
    bTemp = (bTab[iFilterLen / 2] + bTab[iFilterLen / 2 - 1]) / 2;
      return bTemp;
}

void stampaValori () {
    Serial.print("TDS Value:");
    Serial.print(tds,0);
    Serial.println("ppm");

    Serial.print("pH Val: ");
    Serial.println(ph);

    if(acqua > 0.5) {
        Serial.print("Il livello dell'acqua è sufficiente: ");
        Serial.println(acqua);
    }
    else if(acqua >0.1)
        Serial.print("Aggiungere Acqua, sistema a rischio!: ");
    else
        Serial.print("Emergenza, la pompa è stata spenta per evitare problemi: ");
    Serial.println(acqua);

    if(luce > 0.5)
        Serial.print("La luce è sufficiente: ");
    else
        Serial.print("C'è poca luce nella stanza: ");
    Serial.println(luce);

    Serial.print("Temperatura: ");
    Serial.print(temp);
    Serial.println(" C");

    

    Serial.println("");
}

def _test():
    print ("Start: Arduino Manager")

if __name__ == "__main__":
    _test()
