import requests    
import json     
import time  
import random 
import psutil

from gpiozero import CPUTemperature
# tehdään listat plottaamista varten
alfat = []
xt = []
yt = []
zt = []

sade = 10
alfa = 0


#Funktio lämpötilan saamiseen
def cpu_temp():
    temp = CPUTemperature()
    cpu_temp = round(temp.temperature,1)

    return cpu_temp

while alfa < 10:

    measurement = { }
    measurement['alfa'] = alfa
    measurement['x'] = psutil.cpu_percent(interval=5)
    measurement['y'] = psutil.virtual_memory().percent
    measurement['z'] = cpu_temp()

    # lisätään vielä listoihin plottaamista varten
    alfat.append(measurement['alfa'])
    xt.append(measurement['x'])
    yt.append(measurement['y'])
    zt.append(measurement['z'])

    # muunna json-muotoon 
    s = json.dumps(measurement)
    # TODO: lähetä data HTTP Postilla serverille
    response = requests.post("http://localhost:5000/uusimittaus", data = s)

    print(s)
    time.sleep(0.5)

    alfa += 0.1
# plotataan
