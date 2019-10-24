import paho.mqtt.client as mqtt
import pymysql
import time

MQTT_Terima = "coeg/1"
data = ""
d = "0,0,0"

con = pymysql.connect( db="raspberry",
                       user="root",
                       passwd="",
                       host="localhost",
                       port = 3306)
cursor = con.cursor()
sql = "INSERT INTO gateway (no1, no2, no3) VALUES (%s, %s, %s)"

def on_connect(client, userdata, flags, rc):
    print("connect with result code", str(rc))
    client.subscribe(MQTT_Terima)

def on_message(cient, userdata, msg):
    # kamus global
    global data
    global d

    print('--------------------------------')
    print(msg.topic + " " + str(msg.payload.decode("utf-8")))

    data = msg.payload.decode("utf-8")
    d = data.split(',')
    # print('pesan : ', data)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)

valid = ''
while True:
    client.loop_start()
    value = [(d[0],d[1],d[2])]
    if data != valid:
        print('pesan : ', value)
        cursor.executemany(sql, value)
        con.commit()
        valid = data
    time.sleep(1)