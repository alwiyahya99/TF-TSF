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
import time
import datetime

MQTT_Terima = "coeg/1"
MQTT_Kirim = "coeg/2"
MQTT_Suhu_kirim = "coeg/3"

def on_connect(client, userdata, flags, rc):
        print("connect with result code", str(rc))
        client.subscribe(MQTT_Terima)

def on_message(cient, userdata, msg):

        print('--------------------------------')
        print(msg.topic + " " + str(msg.payload))

        a = str(msg.payload)
        waktuSet = a.split("'")
        waktuSekarang = datetime.datetime.now()
        menit = str(waktuSekarang.minute)

        # print('waktu permintaan : ', waktuSet[1])
        # print('waktu sekarang : ', menit)
        print('Request : ', waktuSet[1])
        print('waktu sekarang : ', menit)

        print('Request : ', waktuSet[1])
        Temperature = 20
        Humidity = 60

        if waktuSet[1] == "reqTemp":
            publish.single(MQTT_Kirim, Temperature, hostname="broker.hivemq.com")
            print("Pesan  telah di bales")
            time.sleep(1)

        elif waktuSet[1] == "reqHum":
            publish.single(MQTT_Kirim, Humidity, hostname="broker.hivemq.com")
            print("Pesan  telah di bales")
            time.sleep(1)

        elif waktuSet[1] == "reqHum,reqTemp" or waktuSet[1] == "reqTemp,reqHum":
            publish.single(MQTT_Kirim, Temperature, hostname="broker.hivemq.com")
            publish.single(MQTT_Kirim, Humidity, hostname="broker.hivemq.com")
            print("Pesan  telah di bales")
            time.sleep(1)

        elif waktuSet[1] == "tanah":
            publish.single(MQTT_Kirim, "Maaf fitur inimasih dalam pengembangan :) ", hostname="broker.hivemq.com")
            print("Pesan  telah di bales")
            time.sleep(1)

        elif msg.payload == b"hai" or msg.payload == b"HAI" or msg.payload == b"Hai" or msg.payload == b"hei":
            print("Hai saya perangkat yang terhubung ke protokol MQTT")
            publish.single(MQTT_Kirim,
                           "Hai saya perangkat yang terhubung ke protokol MQTT, Ada yang bisa saya bantu !!!",
                           hostname="broker.hivemq.com")
            print("Pesan  telah di bales")
            time.sleep(1)

        elif waktuSet[1] == "info":
            print("Hai saya perangkat yang terhubung ke protokol MQTT")
            publish.single(MQTT_Kirim, "Hai saya perangkat yang terhubung ke protokol MQTT yang mempunyai fitur : \n"
                                       "reqTemp -> untuk melihat status temperature udara\n"
                                       "reqHum  -> untuk melihat status kelembaban udara\n"
                                       "tanah   -> masih dalam pengembangan", hostname="broker.hivemq.com")
            print("Pesan  telah di bales")
            time.sleep(1)

        elif waktuSet[1] == "":
            print("Maaf pesan anda kosong, bisa ketikan yang ingin anda perintahkan !!!")
            publish.single(MQTT_Kirim, "Maaf pesan anda kosong,\nbisa ketikan yang ingin anda perintahkan !!!",
                           hostname="broker.hivemq.com")
            print("Pesan  telah di bales")
            time.sleep(1)

        elif waktuSet[1] == "ok":
            print("Terimakasih :)")
            publish.single(MQTT_Kirim, "Terimakasih :)", hostname="broker.hivemq.com")
            print("Pesan  telah di bales")
            time.sleep(1)

        else:
            print("Maaf perintah tidak dikenali")
            publish.single(MQTT_Kirim, "Maaf perintah tidak dikenali,\nmohon ulangi cuy", hostname="broker.hivemq.com")
            print("Pesan  telah di bales")
            time.sleep(1)
        #
        # pesan1 = 'basah'
        # pesan2 = 'kering'
        # while waktuSet[1] != menit:
        #     waktuSekarang = datetime.datetime.now()
        #     menit = str(waktuSekarang.second)
        #     print('Basah-----waktu sekarang : ', waktuSekarang.strftime("%Y-%m-%d %H:%M:%S"))
        #     # print(pesan1)
        #     if pesan1 == 'basah':
        #         print(pesan1)
        #         publish.single(MQTT_Kirim, pesan1, hostname="broker.hivemq.com")
        #         print(" Pesan telah dikirim\n----------------------------------")
        #         pesan1 = 'kering'
        #         pesan2 = 'kering'
        #
        #     time.sleep(1)
        #     while waktuSet[1] == menit:
        #         waktuSekarang = datetime.datetime.now()
        #         menit = str(waktuSekarang.second)
        #         print('Kering-----waktu sekarang : ', waktuSekarang.strftime("%Y-%m-%d %H:%M:%S"))
        #         # print(pesan2)
        #         if pesan2 == 'kering':
        #             print(pesan2)
        #             publish.single(MQTT_Kirim, pesan2, hostname="broker.hivemq.com")
        #             print(" Pesan telah dikirim\nTunggu Sedang Menyiram------------")
        #             pesan2 = 'basah'
        #             pesan1 = 'basah'
        #             time.sleep(10)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)
client.loop_forever()