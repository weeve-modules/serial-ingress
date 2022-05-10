# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import serial # import module
import serial

import json
try:
  # port, GNU / Linux up / dev / ttyUSB0  wait or  Windows up  COM3  wait
  portx="/dev/cu.usbserial-130"
  # baud rate, one of the standard values ：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
  bps=115200
  # timeout setting, None： waiting for operation forever, 0 to return the result of the request immediately, the other values are waiting timeouts ( in seconds ）
  timex=5
  #  open the serial port and get the serial port object
  ser=serial.Serial(portx,bps,timeout=timex)
  #  read json payload
  ser.reset_input_buffer()
  while 1:
       data = ser.readline().decode("utf-8")

  #result=ser.read(bytes(data, "utf-8"), )
       dict_json = json.loads(data)
       print(dict_json)
  #print(int(data))

  #ser.close()# close the serial port

except json.JSONDecodeError as e:
    print("JSON:", e)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

