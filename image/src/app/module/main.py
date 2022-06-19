"""
All logic related to the module's main application
Mostly only this file requires changes
"""
import serial
import json
from app.weeve.egress import send_data
from app.config import APPLICATION

def module_main():
    """implement module logic here

    Args:
        parsed_data ([JSON Object]): [The output of data_validation function]

    Returns:
        [string, string]: [data, error]
    """
    parity_dict = {
       "None" : serial.PARITY_NONE,
       "Even" : serial.PARITY_EVEN,
       "Odd"  : serial.PARITY_ODD
    }
    if APPLICATION['PARITY'] not in parity_dict:
        raise Exception("Invalid parity")
    try:
        #  open the serial port and get the serial port object
        ser = serial.Serial(APPLICATION['PORT'], int(APPLICATION['BAUD_RATE']), timeout=1,bytesize=int(APPLICATION['DATA_BITS']),parity=parity_dict.get(APPLICATION['PARITY']), stopbits=float(APPLICATION['STOP_BITS']))

        while True:
            #  read json payload
            ser.reset_input_buffer()
            data = ser.readline().decode("ISO-8859-1")
            dict_json = json.loads(data)
            sent=send_data(dict_json)
            if sent:
                print(dict_json)
                print("The data successfully sent")
            else :
                print("Failed to send the data")
    except json.JSONDecodeError as err:
        return None, f"Unable to perform the module logic: {err}"
