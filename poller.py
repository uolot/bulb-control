import time

import bulb
import config
import mqtt


POLL_SLEEP = 10

log = config.get_logger(__name__)

BULB = bulb.discover()
MQTT = mqtt.get_client()

log.info("Starting the polling loop")

while True:
    try:
        power, brightness = bulb.get_state(BULB)
    except Exception:
        log.error("Failed to read bulb state", exc_info=True)
    else:
        log.info("Publishing values")
        MQTT.publish(config.POWER_VALUE_TOPIC, payload=power)
        MQTT.publish(config.BRIGHTNESS_VALUE_TOPIC, payload=brightness)
        log.info("... published")
        log.debug("---- Sleeping for %ds %s", POLL_SLEEP, "-" * 30)
    time.sleep(POLL_SLEEP)
