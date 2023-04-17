
from gpiozero import CPUTemperature

def cpu_temp():
    temp = CPUTemperature()
    cpu_temp = round(temp.temperature,1)

    return cpu_temp