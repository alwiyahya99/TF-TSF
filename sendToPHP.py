import requests
import time
#
# temp = str(1)
# hum = str(0)
# press = str(20)
# status = 'basah'
# while True:
#     ##MENGIRIM DATA KE PHP DENGAN METODE POST
#     # kirim = requests.post("http://IoT.alwiyahyamuljabar.xyz/add_data.php?temp=" + temp +
#     #                                                                     "&hum=" + hum +
#     #                                                                     "&pr=" + press +
#     #                                                                     "&st=" + status)
# #
#     ##MENGAMBIL DATA DARI PHP DENGAN METODE GET
#     req = requests.get('http://iot.alwiyahyamuljabar.xyz/Android/getData.php')
#     data = req.json()
#     print("Status Relay : ",data["status"])
# #     print(kirim)
#     time.sleep(5)
#     req = requests.get('http://iot.alwiyahyamuljabar.xyz/Android/getDataWaktu.php')
#     data = req.json()
#     print("Status Relay : ",data["jadwal"])
# #     print(kirim)
#     time.sleep(1)

# #
# # import time
# #
# # a = 0
# # times = 0
# #
# # def getWaktu():
# #     global times
# #     times = 4
# #
# # def getDataTemp(a):
# #     while True:
# #         getWaktu()
# #         a = a + 1
# #         print(a)
# #         if a == times:
# #             break
# #         time.sleep(1)
# #
# # getDataTemp(a)
# import paho.mqtt.client as mqtt
# import paho.mqtt.publish as publish
# import requests
# import time
# import datetime
# from firebase import firebase
# MQTT_Terima = "coeg/1"
# MQTT_Kirim = "coeg/2"

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
#     waktuSekarang = datetime.datetime.now()
#     menit = str(waktuSekarang.strftime("%H:%M:%S"))
#
#     while stop != menit:
#         waktuSekarang = datetime.datetime.now()
#         menit = str(waktuSekarang.strftime("%H:%M:%S"))
#         print(menit)
#         print('tanaman basah')
#         time.sleep(1)
#         while stop == menit:
#             waktuSekarang = datetime.datetime.now()
#             menit = str(waktuSekarang.strftime("%H:%M:%S"))
#             print(menit)
#             print('tanaman keiring')
#             time.sleep(1)
# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message
# client.connect("broker.hivemq.com", 1883, 60)
#
# client.loop_forever()
