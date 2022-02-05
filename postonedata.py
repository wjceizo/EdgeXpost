from base_sensore import createSensore,addReading,randomId,postToEdgex
import json
import time

start = time.perf_counter()
carema = createSensore("countcamera1","camera-monitor-profile","HumanCount",randomId(),1602168089665565200)
carema = addReading(carema,randomId(),1602168089665565202,"countcamera1","HumanCount","camera-monitor-profile","Int16","5")
carema = addReading(carema,randomId(),1602168089665565202,"countcamera1","CanineCount","camera-monitor-profile","Int16","8")
postToEdgex(carema,"http://localhost:59880/api/v2/event/camera-monitor-profile/countcamera1/HumanCount")

end = time.perf_counter()
print("The function run time is : %.03f seconds" %(end-start))


start = time.perf_counter()
randomInt = createSensore("Random-Integer-Device","Random-Integer-Device","Int64",randomId(),1643276926854463000)
randomInt = addReading(randomInt,randomId(),1643276926854463000,"Random-Integer-Device","Int64","Random-Integer-Device","Int64","-1769805107834189082")
postToEdgex(randomInt,"http://localhost:59880/api/v2/event/Random-Integer-Device/Random-Integer-Device/Int64")

end = time.perf_counter()
print("The function run time is : %.03f seconds" %(end-start))