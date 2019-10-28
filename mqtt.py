# mqtt chating dengan alat
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time

MQTT_Kirim = "coeg/1"
MQTT_Terima = "coeg/4"

def on_connect(client, userdata, flags, rc):
    nilai = input('Masukan perintah : ')
    publish.single(MQTT_Kirim, nilai, hostname="broker.hivemq.com")
    print("Done")

    print("connect with result code", str(rc))
    client.subscribe(MQTT_Terima)

def on_message(cient, userdata, msg):

    #print(msg.topic+" "+str(msg.payload))

    print('topic : '+ msg.topic)
    a = str(msg.payload)
    waktuSet = a.split("'")
    print('Nilai : ', waktuSet[1])

    nilai = input('Masukan perintah : ')
    publish.single(MQTT_Kirim, nilai, hostname="broker.hivemq.com")
    print("Done")

    # a = str(msg.payload)
    # hasil = a.split(" ")
    # print(hasil[0])

    '''
    if msg.payload == b"on":
        print("Led Nyala")
        publish.single(MQTT_Topic, "Led Telah Nyala", hostname="broker.hivemq.com")
        print("Pesan  telah di bales")
        time.sleep(1)

    elif msg.payload == b"off":
        print("Led OFF")
        publish.single(MQTT_Topic, "Led Telah Mati", hostname="broker.hivemq.com")
        print("Pesan  telah di bales")
        time.sleep(1)

    elif msg.payload == b"hai" or msg.payload == b"HAI" or msg.payload == b"Hai" or msg.payload == b"hei":
        print("Hai saya perangkat yang terhubung ke protokol MQTT")
        publish.single(MQTT_Topic, "Hai saya perangkat yang terhubung ke protokol MQTT, Ada yang bisa saya bantu !!!", hostname="broker.hivemq.com")
        print("Pesan  telah di bales")
        time.sleep(1)

    elif msg.payload == b"info":
        print("Hai saya perangkat yang terhubung ke protokol MQTT")
        publish.single(MQTT_Topic, "on, off, status", hostname="broker.hivemq.com")
        print("Pesan  telah di bales")
        time.sleep(1)

    elif msg.payload == b"":
        print("Maaf pesan anda kosong, bisa ketikan yang ingin anda perintahkan !!!")
        publish.single(MQTT_Topic, "Maaf pesan anda kosong,\nbisa ketikan yang ingin anda perintahkan !!!", hostname="broker.hivemq.com")
        print("Pesan  telah di bales")
        time.sleep(1)

    elif msg.payload == b"ok":
        print("Terimakasih :)")
        publish.single(MQTT_Topic, "Terimakasih :)", hostname="broker.hivemq.com")
        print("Pesan  telah di bales")
        time.sleep(1)

    else:
        print("Maaf perintah tidak dikenali")
        publish.single(MQTT_Topic, "Maaf perintah tidak dikenali,\nmohon ulangi cuy", hostname="broker.hivemq.com")
        print("Pesan  telah di bales")
        time.sleep(1)
    '''

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)
client.loop_forever()

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("connect with result code", str(rc))
    client.subscribe("coeg/1")


def on_message(cient, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

    if msg.payload == "ON":
        print("Led ON")

    if msg.payload == "OFF":
        print("Led OFF")


# try:
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
#
# except:
#     print('jaringan jelek')

client.loop_forever()