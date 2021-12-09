from nanpy  import ArduinoApi, SerialManager
import time

print('ARDUINO CONNECTION!')

connection = SerialManager(device='COM3')
arduino = ArduinoApi(connection=connection)

#git arduino.pinMode(12, arduino.OUTPUT)