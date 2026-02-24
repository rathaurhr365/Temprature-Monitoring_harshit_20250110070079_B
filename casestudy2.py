import random
import time
min_temprature=int(input("enter the minimum temprature: "))
max_tamprature=int(input("enter the maximum temprature: "))
while True:
    temprature = random.randint(1,100)
    if temprature>max_tamprature:
        print("Alert: temprature is too high, temp=",temprature)
        time.sleep(2)
    elif temprature<min_temprature:
        print("Alert: temprature is too low, temp=",temprature)
        time.sleep(2)
    else:
        print("temprature is within acceptable limits, temp=",temprature)
        time.sleep(2)