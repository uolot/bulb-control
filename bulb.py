import time

from pyHS100 import Discover

import config


log = config.get_logger(__name__)


def discover():
    log.info("Discovering devices")
    devices = Discover.discover()
    while not devices:
        log.warning("... no devices found, retrying in 5 seconds")
        time.sleep(5)
        devices = Discover.discover()
    bulb = next(iter(devices.values()))
    log.info("... found: %s at %s", bulb.alias, bulb.host)
    return bulb


def get_state(bulb):
    log.info("Reading bulb state")
    state = bulb.get_light_state()
    power = state.get("on_off", 0)
    brightness = state.get("brightness", 0)
    log.info("... power: %d", power)
    log.info("... brightness: %d", brightness)
    return power, brightness


def set_power(bulb, power):
    if power:
        bulb.turn_on()
    else:
        bulb.turn_off()
    return 1 if bulb.is_on() else 0


def set_brightness(bulb, brightness):
    bulb.brightness = brightness
    return bulb.brightness
