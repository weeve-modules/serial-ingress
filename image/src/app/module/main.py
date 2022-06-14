"""
All logic related to the module's main application
Mostly only this file requires changes
"""
import serial
import json
from app.weeve.egress import send_data
from app.config import APPLICATION

<<<<<<< HEAD
def parity_translation(sParity=APPLICATION['PARITY']):
=======
sParity=APPLICATION['PARITY']
def switch_demo(sParity):
>>>>>>> c0f28a2ded11f8720b30dd3dc799fb30ba26ae34
    switcher = {
       "None" : "N",
       "Even" : "E",
        "Odd" : "O"
    }
    return switcher.get(sParity, lambda: "Invalid parity")
def module_main():
    """implement module logic here

    Args:
        parsed_data ([JSON Object]): [The output of data_validation function]

    Returns:
        [string, string]: [data, error]
    """
    try:
        #  open the serial port and get the serial port object
<<<<<<< HEAD
        ser = serial.Serial(APPLICATION['PORT'], APPLICATION['BAUD_RATE'], timeout=1,bytesize=APPLICATION['DATA_BITS'],parity=parity_translation(), stopbits=APPLICATION['STOP_BITS'])
        while True:
        #  read json payload
         ser.reset_input_buffer()
         data = ser.readline().decode("ISO-8859-1")
         dict_json = json.loads(data)
         sent=send_data(dict_json)
         if sent:
          print("SUCCESS"),print("failed")
=======
        ser = serial.Serial(APPLICATION['PORT'], APPLICATION['BAUD_RATE'], timeout=1,bytesize=APPLICATION['DATA_BITS'],parity=switch_demo(sParity), stopbits=APPLICATION['STOP_BITS'])
        while True:
          #  read json payload
          ser.reset_input_buffer()
          data = ser.readline().decode("ISO-8859-1")
          dict_json = json.loads(data)
          sent=send_data(dict_json)
          if sent:
            print("SUCCESS"),print("failed")
>>>>>>> c0f28a2ded11f8720b30dd3dc799fb30ba26ae34
          print(dict_json)
    except json.JSONDecodeError as e:
      return None, f"Unable to perform the module logic: {e}"
