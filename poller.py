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
    log.info("Updating bulb state")
    bulb.publish_current_state(bulb, MQTT)

    log.debug("---- Sleeping for %ds %s", POLL_SLEEP, "-" * 30)
    time.sleep(POLL_SLEEP)
