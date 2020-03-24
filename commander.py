import bulb
import config
import mqtt


log = config.get_logger(__name__)

BULB = bulb.discover()
MQTT = mqtt.get_client()


def publish_current_state(client):
    log.info("... reading new state")
    power, brightness = bulb.get_state(BULB)
    log.info("... publishing new state, power: %s, brightness: %s", power, brightness)
    client.publish(config.POWER_VALUE_TOPIC, payload=power)
    client.publish(config.BRIGHTNESS_VALUE_TOPIC, payload=brightness)


def on_message(client, obj, message):
    log.info(f"Received message on topic {message.topic}: {message.payload}")

    if message.topic == config.POWER_COMMAND_TOPIC:
        power = int(message.payload.decode())
        log.info(f"... got new power state: %s", power)

        log.info("... turning bulb %s", "on" if power == 1 else "off")
        power = bulb.set_power(BULB, power)

        publish_current_state(client)
        log.info("... ok")

    elif message.topic == config.BRIGHTNESS_COMMAND_TOPIC:
        brightness = int(message.payload.decode())
        log.info(f"... got new brightness level: %s", brightness)

        log.info("... setting new brightness")
        brightness = bulb.set_brightness(BULB, brightness)

        publish_current_state(client)
        log.info("... ok")


log.info("Subscribing to topics")
MQTT.on_message = on_message
MQTT.subscribe(config.POWER_COMMAND_TOPIC)
MQTT.subscribe(config.BRIGHTNESS_COMMAND_TOPIC)

log.info("Starting client loop")
MQTT.loop_forever()
