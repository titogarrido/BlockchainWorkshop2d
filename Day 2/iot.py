import requests, random

for i in range(0,5):
    r = requests.post('http://148.100.98.42:3000/api/TemperatureReading', data = {'centigrade':str(random.randint(11,20)), 'shipment': 'SHIP_002'})
    print r.text

