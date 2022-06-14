"""
All logic related to the module's main application
Mostly only this file requires changes
"""
import serial
import json
from app.weeve.egress import send_data
from app.config import APPLICATION
def parity_translation(serial_parity=APPLICATION['PARITY']):
    switcher = {
       "None" : serial.PARITY_NONE,
       "Even" : serial.PARITY_EVEN,
       "Odd"  : serial.PARITY_ODD
    }
    try:
        return switcher.get(serial_parity)
    except KeyError:
        print("Invalidate parity")
def module_main():
    """implement module logic here

    Args:
        parsed_data ([JSON Object]): [The output of data_validation function]

    Returns:
        [string, string]: [data, error]
    """
    try:
        #  open the serial port and get the serial port object
        ser = serial.Serial(APPLICATION['PORT'], APPLICATION['BAUD_RATE'], timeout=1,bytesize=APPLICATION['DATA_BITS'],parity=parity_translation(), stopbits=APPLICATION['STOP_BITS'])
        while True:
            #  read json payload
            ser.reset_input_buffer()
            data = ser.readline().decode("ISO-8859-1")
            dict_json = json.loads(data)
            sent=send_data(dict_json)
            if sent:
                print("The data successfully sent")
                print(dict_json)
            else :
                print("Failed to send the data")
    except json.JSONDecodeError as err:
        return None, f"Unable to perform the module logic: {err}"
