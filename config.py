import logging
import os


POWER_COMMAND_TOPIC = os.getenv("POWER_COMMAND_TOPIC")
BRIGHTNESS_COMMAND_TOPIC = os.getenv("BRIGHTNESS_COMMAND_TOPIC")
POWER_VALUE_TOPIC = os.getenv("POWER_VALUE_TOPIC")
BRIGHTNESS_VALUE_TOPIC = os.getenv("BRIGHTNESS_VALUE_TOPIC")

MQTT_USERNAME = os.getenv("MQTT_USERNAME")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")
MQTT_HOST = os.getenv("MQTT_HOST")
MQTT_PORT = int(os.getenv("MQTT_PORT"))


def get_logger(name):
    # formatter = logging.Formatter(logging.BASIC_FORMAT)
    formatter = logging.Formatter("%(asctime)s %(message)s")
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    log = logging.getLogger(name)
    log.addHandler(handler)
    log.setLevel(logging.DEBUG)
    return log
