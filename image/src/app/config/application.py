"""
All constants specific to the application
"""
from app.utils.env import env


APPLICATION = {
    "Port": env("Port", "/dev/cu.usbserial-1130"),
    "Baud_Rate": env("Baud rate", "115200"),
}
