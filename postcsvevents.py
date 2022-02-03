from base_sensore import createSensore, addReading, randomId, postToEdgex
import csv
import time
import random


with open("test.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    fieldnames = next(reader)  
    csv_reader = csv.DictReader(
        f, fieldnames=fieldnames
    )  
    events = []
    for row in csv_reader:
        d = {}
        for k, v in row.items():
            d[k] = v
        events.append(d)
for event in events:
    event["time"] = int(event["time"])
events = sorted(events, key=lambda i: i["time"])
# print(events)


eventslength = len(events)
for (
    i,
    event,
) in enumerate(events):
    timens = time.time_ns()
    if event["time"] == events[i - 1]["time"] and i > 0:
        # print("重复")
        # print(event["deviceName"])
        sensore = addReading(
            sensore,
            randomId(),
            timens,
            event["deviceName"],
            event["resourceName"],
            event["profileName"],
            event["valueType"],
            event["value"],
        )
        if i + 1 < eventslength:
            if event["time"] != events[i + 1]["time"]:
                url = (
                    "http://localhost:59880/api/v2/event/"
                    + event["profileName"]
                    + "/"
                    + event["deviceName"]
                    + "/"
                    + event["sourceName"]
                )
                postToEdgex(sensore, url)
                time.sleep(1)
        elif i == eventslength - 1:
            url = (
                "http://localhost:59880/api/v2/event/"
                + event["profileName"]
                + "/"
                + event["deviceName"]
                + "/"
                + event["sourceName"]
            )
            postToEdgex(sensore, url)
            time.sleep(1)

    else:
        # print("新开一个")
        # print(event["deviceName"])
        sensore = event["deviceName"]
        sensore = createSensore(
            event["deviceName"],
            event["profileName"],
            event["sourceName"],
            randomId(),
            timens,
        )
        sensore = addReading(
            sensore,
            randomId(),
            timens,
            event["deviceName"],
            event["resourceName"],
            event["profileName"],
            event["valueType"],
            event["value"],
        )
        if i + 1 < eventslength:
            if event["time"] != events[i + 1]["time"]:
                url = (
                    "http://localhost:59880/api/v2/event/"
                    + event["profileName"]
                    + "/"
                    + event["deviceName"]
                    + "/"
                    + event["sourceName"]
                )
                postToEdgex(sensore, url)
                time.sleep(1)
        elif i == eventslength - 1:
            url = (
                "http://localhost:59880/api/v2/event/"
                + event["profileName"]
                + "/"
                + event["deviceName"]
                + "/"
                + event["sourceName"]
            )
            postToEdgex(sensore, url)
            time.sleep(1)
