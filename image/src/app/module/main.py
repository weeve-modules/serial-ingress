"""
All logic related to the module's main application
Mostly only this file requires changes
"""

import serial
import json

from app.config import APPLICATION

def module_main():
    """implement module logic here

    Args:
        parsed_data ([JSON Object]): [The output of data_validation function]

    Returns:
        [string, string]: [data, error]
    """
    try:
        #  open the serial port and get the serial port object
        ser = serial.Serial(APPLICATION['PORT'], APPLICATION['BAUD_RATE'], timeout=1)
        while 1:
            ser.reset_input_buffer()
            #  read json payload
            data = ser.readline().decode("ISO-8859-1")
            dict_json = json.loads(data)
            print( dict_json)
            return dict_json, None
   
    except ser.SerialException  as e:       
      return None, f"Unable to perform the module logic: {e}"
