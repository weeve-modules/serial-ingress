"""
All logic related to the module's main application
Mostly only this file requires changes
"""

import serial
import json
import threading
from app.weeve.egress import send_data
from app.config import APPLICATION

#dict_json={}
ser = serial.Serial(APPLICATION['PORT'], APPLICATION['BAUD_RATE'], timeout=1)
def readserial():
    while 1:
            #ser.inWaiting() > 0:
        # ser.reset_input_buffer()
        #  read json payload
        ser.reset_input_buffer()
        data = ser.readline().decode("ISO-8859-1")
        dict_json = json.loads(data)
        sent=send_data(dict_json)
        print(dict_json)

def module_main():
    """implement module logic here

    Args:
        parsed_data ([JSON Object]): [The output of data_validation function]

    Returns:
        [string, string]: [data, error]
    """
    thread = threading.Thread(target=readserial)
    try:
        #  open the serial port and get the serial port object
         thread.start()  
         #while 1:
            
            #  read json payload
           
          
            
    except json.JSONDecodeError as e:
            return None, f"Unable to perform the module logic: {e}"
