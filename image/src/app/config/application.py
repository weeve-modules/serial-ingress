"""
All constants specific to the application
"""
from app.utils.env import env
APPLICATION = {
    "PORT":      env("PORT","/dev/ttyUSB0"),
    "BAUD_RATE": env("BAUD_RATE","115200"),
    "DATA_BITS": env("DATA_BITS",serial.EIGHTBITS),
    "PARITY":    env("PARITY","None"),
    "STOP_BITS": env("STOP_BITS",serial.STOPBITS_ONE)
}
