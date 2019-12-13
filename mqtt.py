import paho.mqtt.client as mqtt

import config

log = config.get_logger(__name__)


def get_client():
    log.info("Connecting to MQTT broker")
    client = mqtt.Client()
    client.username_pw_set(config.MQTT_USERNAME, config.MQTT_PASSWORD)
    client.connect(config.MQTT_HOST, port=config.MQTT_PORT)
    log.info("... connected")
    return client
