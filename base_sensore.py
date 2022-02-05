import json
import uuid
import requests
import sys, getopt


def createSensore(deviceName, profileName, sourceName, sensoreid, origin):
    """
    origin is int number, else all string.
    """
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


def addReading(
    sensore, readingid, origin, deviceName, resourceName, profileName, valueType, value
):
    """
    sensore is a dict ,origin is int number, else all string.
    """
    reading = {
        "id": readingid,
        "origin": origin,
        "deviceName": deviceName,
        "resourceName": resourceName,
        "profileName": profileName,
        "valueType": valueType,
        "value": value,
    }
    sensore["event"]["readings"].append(reading)
    return sensore


def randomId():
    name = "edgex_name"
    namespace = "edgex_namespace"
    uid = str(uuid.uuid1())
    return uid


def postToEdgex(sensore, url):
    """
    sensor is dict ,url is string(like "http://localhost:59880/api/v2/event/camera-monitor-profile/countcamera1/HumanCount").
    """
    j = json.dumps(sensore)
    url = url
    payload = j
    headers = {"CONTENT-TYPE": "application/JSON"}
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def cys(argv):
    """
    默认的csv为当前目录下test.csv，默认的ip_host为localhost:59880。
    """
    inputcsv = "test.csv"
    inputhost = "localhost:59880"
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print("postcsvevents.py -i <inputcsv> -o <inputhost>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("postcsvevents.py -i <inputcsv> -o <inputhost>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputcsv = arg
        elif opt in ("-o", "--ofile"):
            inputhost = arg
    return inputcsv, inputhost
