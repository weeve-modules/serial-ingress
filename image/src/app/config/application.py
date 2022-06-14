"""
All constants specific to the application
"""
from app.utils.env import env
APPLICATION = {
    "PORT":      env("PORT","/dev/ttyUSB0"),
    "BAUD_RATE": env("BAUD_RATE","115200"),
<<<<<<< HEAD
    "DATA_BITS": env("DATA_BITS",serial.EIGHTBITS),
    "PARITY":    env("PARITY","None"),
    "STOP_BITS": env("STOP_BITS",serial.STOPBITS_ONE)
=======
    "DATA_BITS": env("DATA_BITS","EIGHTBITS"),
    "PARITY":    env("PARITY",'None'),
    "STOP_BITS": env("STOP_BITS","STOPBITS_ONE")
>>>>>>> c0f28a2ded11f8720b30dd3dc799fb30ba26ae34
}
