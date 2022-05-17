"""
All constants specific to the application
"""
from app.utils.env import env


APPLICATION = {
    Port: env("USB Port", "/dev/cu.usbserial-130"),
    Baud_Rate: env("Baud rate", "9600"),
}
