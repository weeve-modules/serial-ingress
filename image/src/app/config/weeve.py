"""
All constants specific to weeve
"""
from app.utils.env import env

WEEVE = {
    "MODULE_NAME": env("MODULE_NAME", "serial-ingress"),
    "MODULE_TYPE": env("MODULE_TYPE", "INGRESS")
}
