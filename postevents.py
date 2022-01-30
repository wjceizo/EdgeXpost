from base_sensore import createSensore, addReading, randomId, postToEdgex
import json
import time

with open("events.json", "r", encoding="utf8") as fp:
    json_data = json.load(fp)
data = json_data

for event in data["events"]:
    sensore = event["deviceName"]
    sensore = createSensore(
        event["deviceName"],
        event["profileName"],
        event["sourceName"],
        randomId(),
        event["origin"],
    )
    for reading in event["readings"]:
        sensore = addReading(
            sensore,
            randomId(),
            reading["origin"],
            reading["deviceName"],
            reading["resourceName"],
            reading["profileName"],
            reading["valueType"],
            reading["value"],
        )
    url = (
        "http://localhost:59880/api/v2/event/"
        + event["profileName"]
        + "/"
        + event["deviceName"]
        + "/"
        + event["sourceName"]
    )
    postToEdgex(sensore, url)
    time.sleep(2)
