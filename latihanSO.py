# #
# # setWaktu = 44
# # while True:
# #     b = datetime.datetime.now()
# #     min = b.minute
# #     print(min)
# #     if min == setWaktu:
# #         print('siram tanaman')
# #     else:
# #         print('tanaman basah')
# #     time.sleep(1)
#     # print("Current Year is: %d" % currentDT.year)
#     # print("Current Month is: %d" % currentDT.month)
#     # print("Current Day is: %d" % currentDT.day)
#     # print("Current Hour is: %d" % currentDT.hour)
#     # print("Current Minute is: %d" % currentDT.minute)
#     # print("Current Second is: %d" % currentDT.second)
#     # print("Current Microsecond is: %d" % currentDT.microsecond)
#
#
# #mqtt chating dengan alat
# import paho.mqtt.client as mqtt
# import paho.mqtt.publish as publish
# import time
# import datetime
#
# MQTT_Terima = "coeg/1"
# MQTT_Kirim = "coeg/4"
# MQTT_Suhu_kirim = "coeg/3"
#
# stop = 0
#
# def on_connect(client, userdata, flags, rc):
#         print("connect with result code", str(rc))
#         client.subscribe(MQTT_Terima)
#
# def on_message(cient, userdata, msg):
#
#         print('--------------------------------')
#         print(msg.topic + " " + str(msg.payload))
#
#         a = str(msg.payload)
#         waktuSet = a.split("'")
#         waktuSekarang = datetime.datetime.now()
#         menit = str(waktuSekarang.minute)
#
#         print('waktu permintaan : ', waktuSet[1])
#         print('waktu sekarang : ', menit)
#         #
#         # print('Request : ', waktuSet[1])
#         # Temperature = 20
#         # Humidity = 60
#         #
#         # if waktuSet[1] == "reqTemp":
#         #     publish.single(MQTT_Kirim, Temperature, hostname="broker.hivemq.com")
#         #     print("Pesan  telah di bales")
#         #     time.sleep(1)
#         #
#         # if waktuSet[1] == "reqHum":
#         #     publish.single(MQTT_Kirim, Humidity, hostname="broker.hivemq.com")
#         #     print("Pesan  telah di bales")
#         #     time.sleep(1)
#         #
#         pesan1 = 'basah'
#         pesan2 = 'kering'
#         while waktuSet[1] != menit:
#             waktuSekarang = datetime.datetime.now()
#             menit = str(waktuSekarang.second)
#             print('Basah-----waktu sekarang : ', waktuSekarang.strftime("%Y-%m-%d %H:%M:%S"))
#             # print(pesan1)
#             if pesan1 == 'basah':
#                 print(pesan1)
#                 publish.single(MQTT_Kirim, pesan1, hostname="broker.hivemq.com")
#                 print(" Pesan telah dikirim\n----------------------------------")
#                 pesan1 = 'kering'
#                 pesan2 = 'kering'
#
#             time.sleep(1)
#             while waktuSet[1] == menit:
#                 waktuSekarang = datetime.datetime.now()
#                 menit = str(waktuSekarang.second)
#                 print('Kering-----waktu sekarang : ', waktuSekarang.strftime("%Y-%m-%d %H:%M:%S"))
#                 # print(pesan2)
#                 if pesan2 == 'kering':
#                     print(pesan2)
#                     publish.single(MQTT_Kirim, pesan2, hostname="broker.hivemq.com")
#                     print(" Pesan telah dikirim\nTunggu Sedang Menyiram------------")
#                     pesan2 = 'basah'
#                     pesan1 = 'basah'
#                     time.sleep(10)
#
# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message
#
# client.connect("broker.hivemq.com", 1883, 60)
# client.loop_forever()


#
# setWaktu = 44
# while True:
#     b = datetime.datetime.now()
#     min = b.minute
#     print(min)
#     if min == setWaktu:
#         print('siram tanaman')
#     else:
#         print('tanaman basah')
#     time.sleep(1)
    # print("Current Year is: %d" % currentDT.year)
    # print("Current Month is: %d" % currentDT.month)
    # print("Current Day is: %d" % currentDT.day)
    # print("Current Hour is: %d" % currentDT.hour)
    # print("Current Minute is: %d" % currentDT.minute)
    # print("Current Second is: %d" % currentDT.second)
    # print("Current Microsecond is: %d" % currentDT.microsecond)

#mqtt chating dengan alat
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import requests
import time
import datetime
from firebase import firebase

fb = firebase
MQTT_Terima = "coeg/1"
MQTT_Kirim = "coeg/2"

stop = ""
def putFirebase():
    global result1
    global result2
    global result3
    global result4
    firebase = fb.FirebaseApplication('https://watering-apps.firebaseio.com/', None)
    result1 = firebase.put('/watering-apps/keterangan', 'kelembapan', hum)
    result2 = firebase.put('/watering-apps/keterangan', 'suhu', temp)
    result3 = firebase.put('/watering-apps/keterangan', 'soil', press)
    result4 = firebase.put('/watering-apps/keterangan', 'time', menit)
    result4 = firebase.put('/watering-apps', 'status', status)

def sendDataPHP():
    requests.post("http://IoT.alwiyahyamuljabar.xyz/add_data.php?temp=" + str(temp) +
                                                                  "&hum=" + str(hum) +
                                                                  "&pr=" + str(press))  # mengirim data ke php

def sendDataPHP2():
    requests.post("http://IoT.alwiyahyamuljabar.xyz/add_data.php?temp=" + str(temp) +
                                                                  "&hum=" + str(hum) +
                                                                  "&pr=" + str(press) +
                                                                  "&st=" + pesan2)  # mengirim data ke php

def sendDataAlatPHP():
    requests.post("http://IoT.alwiyahyamuljabar.xyz/add_DataAlat.php?status=" + str(status))  # mengirim data ke php

def getDataPHP():
    global Req
    req = requests.get('http://iot.alwiyahyamuljabar.xyz/Android/getDataAlat.php')
    data = req.json()
    Req = data["status"]
    print("Status Relay : ",data["status"])

def getDataWaktuPHP():
    global stop
    req = requests.get('http://iot.alwiyahyamuljabar.xyz/Android/getDataWaktu.php')
    data = req.json()
    stop = data["jadwal"]
    print("Status waktu : ",data["jadwal"])

# def on_connect(client, userdata, flags, rc):
#     print("connect with result code", str(rc))
#     client.subscribe(MQTT_Terima)
#
# def on_message(cient, userdata, msg):
#     # kamus global
#     global stop
#
#     print('--------------------------------')
#     print(msg.topic + " " + str(msg.payload.decode("utf-8")))
#
#     stop = msg.payload.decode("utf-8")
#     print('pesan : ', stop)
#
# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message
# client.connect("broker.hivemq.com", 1883, 60)

temperature = 30
humidity = 30
output2 = 30

temp = "%.1f" % temperature
hum = "%.1f" % humidity
press = "%.1f" % output2

while True:
    # client.loop_start()
    getDataWaktuPHP()
    time.sleep(1)
    waktuSekarang = datetime.datetime.now()
    menit = str(waktuSekarang.strftime("%H:%M:%S"))
    # waktu = str(waktuSekarang.strftime("%H:%M:%S"))

    print('waktu permintaan : ', stop)
    print('waktu sekarang : ', menit)

    pesan1 = 'kering'
    pesan2 = 'kering'
    while stop != menit or Req == "Off":
        getDataPHP()
        getDataWaktuPHP()
        sendDataPHP()
        waktuSekarang = datetime.datetime.now()
        menit = str(waktuSekarang.strftime("%H:%M:%S"))
        print('Basah : ', menit)
        print('Req : ', Req)
        # print(pesan1)
        temp = "%.1f" % temperature
        hum = "%.1f" % humidity
        press = "%.1f" % output2
        statusGarden = str('{0},{1:0.1f},{2:0.1f}'.format(pesan1, temperature, humidity))
        if pesan1 == 'basah':
            # print(pesan1)
            # publish.single(MQTT_Kirim, pesan1, hostname="broker.hivemq.com")
            print(" Sedang Mengirim Pesan \n----------------------------------")
            putFirebase()
            # publish.single(MQTT_Kirim, statusGarden, hostname="broker.hivemq.com") #megirim data ke mqtt
            print(" Pesan status '",statusGarden,"' telah dikirim\n----------------------------------")
            sendDataPHP2()
            pesan1 = 'kering'
            pesan2 = 'kering'
            temperature += 1
            humidity += 2
        time.sleep(1)

        while stop == menit or Req == "On":
            status = "Off"
            getDataPHP()
            sendDataAlatPHP()
            waktuSekarang = datetime.datetime.now()
            menit = str(waktuSekarang.strftime("%H:%M:%S"))
            print('Kering : ', menit)
            # print(pesan2)
            statusGarden = str('{0},{1:0.1f},{2:0.1f}'.format(pesan1, temperature, humidity))
            print(statusGarden)
            if pesan2 == 'kering':
                # print(pesan2)
                # publish.single(MQTT_Kirim, pesan2, hostname="broker.hivemq.com")
                print(" Sedang Mengirim Pesan\n----------------------------------")
                putFirebase()
                sendDataPHP2()
                firebase = fb.FirebaseApplication('https://https://watering-apps.firebaseio.com/', None)
                # publish.single(MQTT_Kirim, statusGarden, hostname="broker.hivemq.com")
                print(" Pesan status '", statusGarden, "' telah dikirim\n----------------------------------")
                pesan1 = 'basah'
                pesan2 = 'basah'
                time.sleep(10)

if stop == "on":
    print("Led Nyala")
    publish.single(MQTT_Kirim, "Led Telah Nyala", hostname="broker.hivemq.com")
    print("Pesan  telah di bales")
    time.sleep(1)

elif stop == "off":
    print("Led OFF")
    publish.single(MQTT_Kirim, "Led Telah Mati", hostname="broker.hivemq.com")
    print("Pesan  telah di bales")
    time.sleep(1)

elif stop == "status":
    print(statusGarden)
    publish.single(MQTT_Kirim, statusGarden, hostname="broker.hivemq.com")
    print("Pesan  telah di bales")
    time.sleep(1)

elif stop == "hai" or stop == "HAI" or stop == "Hai" or stop == "hei":
    print("Hai saya perangkat yang terhubung ke protokol MQTT")
    publish.single(MQTT_Kirim,
                   "Hai saya perangkat yang terhubung ke protokol MQTT. Ada yang bisa saya bantu !!!",
                   hostname="broker.hivemq.com")
    print("Pesan  telah di bales")
    time.sleep(1)

elif stop == "info":
    print("Hai saya perangkat yang terhubung ke protokol MQTT")
    publish.single(MQTT_Kirim, "on, off, status", hostname="broker.hivemq.com")
    print("Pesan  telah di bales")
    time.sleep(1)

elif stop == "":
    print("Maaf pesan anda kosong, bisa ketikan yang ingin anda perintahkan !!!")
    publish.single(MQTT_Kirim, "Maaf pesan anda kosong.\nbisa ketikan yang ingin anda perintahkan !!!",
                   hostname="broker.hivemq.com")
    print("Pesan  telah di bales")
    time.sleep(1)

elif stop == "ok":
    print("Terimakasih :)")
    publish.single(MQTT_Kirim, "Terimakasih :)", hostname="broker.hivemq.com")
    print("Pesan  telah di bales")
    time.sleep(1)

else:
    print("Maaf perintah tidak dikenali")
    publish.single(MQTT_Kirim, "Maaf perintah tidak dikenali.\nmohon ulangi cuy", hostname="broker.hivemq.com")
    print("Pesan  telah di bales")
    time.sleep(1)

# client.loop_forever()