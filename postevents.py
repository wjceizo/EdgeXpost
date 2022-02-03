from base_sensore import createSensore, addReading, randomId, postToEdgex
import json
import time
import random

with open("events.json", "r", encoding="utf8") as fp:
    json_data = json.load(fp)
data = sorted(json_data, key = lambda i: i['time'] )

for event in data:
    # print(event["deviceName"])
    timens = time.time_ns()
    newtimens = timens + random.randint(1,10)
    sensore = event["deviceName"]
    sensore = createSensore(
        event["deviceName"],
        event["profileName"],
        event["sourceName"],
        randomId(),
        timens,
    )
    for reading in event["readings"]:
        sensore = addReading(
            sensore,
            randomId(),
            newtimens,
            event["deviceName"],
            reading["resourceName"],
            event["profileName"],
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
