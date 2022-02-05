from base_sensore import createSensore, addReading, randomId, postToEdgex,cys
import csv
import time
import random
import sys

#默认的csv为当前目录下test.csv，默认的ip_host为localhost:59880
open_csv,ip_host = cys(sys.argv[1:])

with open(open_csv, "r", encoding="utf-8") as f:
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
edgex_url = "http://" + ip_host + "/api/v2/event/"
eventslength = len(events)

init_time = time.perf_counter()

time.sleep(events[0]["time"])

for (i,event) in enumerate(events):
    timens = time.time_ns()
    if event["time"] == events[i - 1]["time"] and event["deviceName"] == events[i - 1]["deviceName"] and event["profileName"] == events[i - 1]["profileName"] and  i > 0:
        # print("repeat this event")
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
        if i  < eventslength -1:
            if event["deviceName"] != events[i + 1]["deviceName"] or event["profileName"] != events[i + 1]["profileName"] or event["time"] != events[i + 1]["time"] :
                url = (edgex_url + event["profileName"] + "/" + event["deviceName"] + "/" + event["sourceName"])
                start = time.perf_counter()
                print("Time:"+str(round((time.perf_counter()-init_time),2)))
                postToEdgex(sensore, url)
                end = time.perf_counter()
                post_time = round(end - start , 2)
                sleep_time = events[i + 1]["time"] - (time.perf_counter()-init_time)  if (events[i + 1]["time"] - (time.perf_counter()-init_time)) > 0 else 0
                time.sleep(sleep_time)
        elif i == eventslength - 1:
            url = (edgex_url + event["profileName"] + "/" + event["deviceName"] + "/" + event["sourceName"])
            print("Time:"+str(round((time.perf_counter()-init_time),2)))
            postToEdgex(sensore, url)

    else:
        # print("new event")
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
        if i  < eventslength -1:
            if event["deviceName"] != events[i + 1]["deviceName"] or event["profileName"] != events[i + 1]["profileName"] or event["time"] != events[i + 1]["time"]:
                url = (edgex_url + event["profileName"] + "/" + event["deviceName"] + "/" + event["sourceName"])
                start = time.perf_counter()
                print("Time:"+str(round((time.perf_counter()-init_time),2)))
                postToEdgex(sensore, url)
                end = time.perf_counter()
                post_time = round(end - start , 2)
                sleep_time = events[i + 1]["time"] - (time.perf_counter()-init_time)  if (events[i + 1]["time"] - (time.perf_counter()-init_time)) > 0 else 0
                time.sleep(sleep_time)
        elif i == eventslength - 1:
            url = (edgex_url + event["profileName"] + "/" + event["deviceName"] + "/" + event["sourceName"])
            print("Time:"+str(round((time.perf_counter()-init_time),2)))
            postToEdgex(sensore, url)

