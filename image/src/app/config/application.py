"""
All constants specific to the application
"""
import serial
from app.utils.env import env

APPLICATION = {
    "PORT": env("PORT","/dev/ttyUSB0"),
    "BAUD_RATE": env("BAUD_RATE","115200"),
     "DATA_BITS": env("DATA_BITS",8),
     "PARITY": env("PARITY",serial.PARITY_NONE),
      "STOP_BITS": env("STOP_BITS",1)
      
}

