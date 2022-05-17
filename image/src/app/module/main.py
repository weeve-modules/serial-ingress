"""
All logic related to the module's main application
Mostly only this file requires changes
"""


def module_main():
    """implement module logic here

    Args:
        parsed_data ([JSON Object]): [The output of data_validation function]

    Returns:
        [string, string]: [data, error]
    """
   try:
    # port
    port = "/dev/cu.usbserial-130"
    #  open the serial port and get the serial port object
    ser = serial.Serial(port, 115200, timeout=1)
    while 1:
        ser.reset_input_buffer()
        #  read json payload
        data = ser.readline().decode("ISO-8859-1")
        dict_json = json.loads(data)
        print(dict_json)
except json.JSONDecodeError as e:
    print("JSON:", e)
