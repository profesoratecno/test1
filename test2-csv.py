import csv
from sense_hat import SenseHat
from datetime import datetime
import os
from time import sleep

dir_path = os.path.dirname(os.path.realpath(__file__))
sense = SenseHat()

data_file = dir_path + '/data.csv'

with open(data_file, 'w') as f:
    writer = csv.writer(f)
    header = ("Date/time", "Temperature", "Humidity")
    writer.writerow(header)

for i in range(10):
    row = (datetime.now(), sense.temperature, sense.humidity)
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)
    sleep(60)
    