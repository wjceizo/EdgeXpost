import json
import uuid
import requests

# origin is int number, else all string.
def createSensore(deviceName, profileName, sourceName, sensoreid, origin):
    baseSensore = {
        "apiVersion": "v2",
        "event": {
            "apiVersion": "v2",
            "deviceName": deviceName,
            "profileName": profileName,
            "sourceName": sourceName,
            "id": sensoreid,
            "origin": origin,
            "readings": [],
        },
    }
    return baseSensore

# sensore is a dict ,origin is int number, else all string.
def addReading(
    sensore, readingid, origin, deviceName, resourceName, profileName, valueType, value):
    reading = {
        "id": readingid,
        "origin": origin,
        "deviceName": deviceName,
        "resourceName": resourceName,
        "profileName": profileName,
        "valueType": valueType,
        "value": value,
    }
    sensore['event']['readings'].append(reading)
    return sensore

def randomId():
    name = "edgex_name"
    namespace = "edgex_namespace"
    uid = str(uuid.uuid1())
    return uid

# sensor is dict ,url is string(like "http://localhost:59880/api/v2/event/camera-monitor-profile/countcamera1/HumanCount").
def postToEdgex(sensore,url):
    j = json.dumps(sensore)
    url = (url)
    payload = j
    headers = {"CONTENT-TYPE": "application/JSON"}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)