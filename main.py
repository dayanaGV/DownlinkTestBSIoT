import requests
import time

# Function to convert string to hex, return a list
def print_string_hex(data):
    lin = ['%02X' % ord(i) for i in data]
    return lin

# Function to convert list to string
def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1

headers = {
'Content-Type': 'application/json',
'Authorization': 'Bearer +token',
}

#El mensaje de prueba ser "hola" más un contador

count=98
for i in range(2):
    print(count)
    lista=  print_string_hex(str(count))
    mensaje= "686f6c61" + listToString(lista)
    data = '{"cmd": "tx", "EUI": "#####", "port": 35, "confirmed": false, "data": "'+mensaje+'", "appid": "####"}'
    response = requests.post('https://us1.loriot.io/1/rest', headers=headers, data=data)
    count+=1
    time.sleep(15)

