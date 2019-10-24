import paho.mqtt.publish as publish
import time
import requests

print('--------------=Menu Pengiriman Data=---------------')
print('1. MQTT')
print('2. WEB SERVER')
pilihan = input('Masukan Pilihan : ')
print('---------------------------------------------------\n')

if pilihan=='1':
    print('MQTT')
    topicCloud = input('Masukan Topic : ')
    alamatHost = input('Masukan Host Broker : ')
    pesan = input('Masukan pesan yang dikirim : ')
    # "broker.hivemq.com"

    while True:
        publish.single(topicCloud, pesan, hostname=alamatHost)
        print("Done")
        time.sleep(1)

elif pilihan=='2':
    print('WEB SERVER')
    alamat = input('Masukan Host WEB SERVER : ')
    suhu = input('Masukan nilai suhu :')
    kelembapan = input('Masukan nilai kelembapan :')

    while True:
        url = "http://"+alamat+"/temperatur/add.php?SUHU=" + str(suhu) + "&KELEMBAPAN=" + str(kelembapan) + "/"
        resp = requests.post(url)
        time.sleep(1)
