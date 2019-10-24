#
# from firebase import firebase
# import datetime
# import time
#
# suhu = 12
#
# firebase = firebase.FirebaseApplication('https://watering-apps.firebaseio.com/', None)
# # while True:
# waktuSekarang = datetime.datetime.now()
# detik = str(waktuSekarang.second)
#
# # # result = firebase.put('/Status','Pompa','Off')
# #
# # result = firebase.put(detik.strftime("%Y-%m-%d %H:%M:%S"), 'status', 'Off')
# # # if detik == 60:
# result = firebase.put('/watering-apps', 'status', 'Off')
# print( waktuSekarang)
# time.sleep(1)

from firebase import firebase
import datetime, time

fb = firebase
control = ""
setWaktu1 = 0
setWaktu2 = 0
jam = 0

hum = 1
temp = 2
press = 3
waktuSekarang = 4
def getFirebase():
    # global control
    # global setWaktu1
    # global setWaktu2
    # firebase = fb.FirebaseApplication('https://https://watering-apps.firebaseio.com/', None)
    # control = firebase.get('/Status/Pompa', '')
    # setWaktu1 = firebase.get('/setWaktu/jam1', '')
    # setWaktu2 = firebase.get('/setWaktu/jam2', '')
    firebase = fb.FirebaseApplication('https://watering-apps.firebaseio.com/', None)
    result1 = firebase.put('/watering-apps/keterangan', 'kelembapan', hum)
    result2 = firebase.put('/watering-apps/keterangan', 'suhu', temp)
    result3 = firebase.put('/watering-apps/keterangan', 'soil', press)
    result4 = firebase.put('/watering-apps/keterangan', 'time', waktuSekarang)

getFirebase()


# def getWaktu():
#     global jam
#     waktuSekarang = datetime.datetime.now()
#     jam = str(waktuSekarang.second)
#
# pesan1 = 'basah'
# pesan2 = 'kering'
# while True:
#     getFirebase()
#     getWaktu()
#     print('waktu permintaan : ', setWaktu1)
#     print('waktu sekarang : ', jam)
#     while setWaktu1 != jam:
#         getFirebase()
#         getWaktu()
#         waktuSekarang = datetime.datetime.now()
#         jam = str(waktuSekarang.second)
#         print('Basah : ', waktuSekarang.strftime("%Y-%m-%d %H:%M:%S"))
#         # print(pesan1)
#         if pesan1 == 'basah':
#             # print(pesan1)
#             # publish.single(MQTT_Kirim, pesan1, hostname="broker.hivemq.com")
#             print(" Pesan status '",pesan1,"' telah dikirim\n----------------------------------")
#             pesan1 = 'kering'
#             pesan2 = 'kering'
#         time.sleep(1)
#
#         while int(setWaktu1) >= int(jam):
#             getFirebase()
#             getWaktu()
#             waktuSekarang = datetime.datetime.now()
#             jam = str(waktuSekarang.second)
#             print('Kering : ', waktuSekarang.strftime("%Y-%m-%d %H:%M:%S"))
#             # print(pesan2)
#             if pesan2 == 'kering':
#                 # print(pesan2)
#                 # publish.single(MQTT_Kirim, pesan2, hostname="broker.hivemq.com")
#                 print(" Pesan telah dikirim\nTunggu Sedang Menyiram------------")
#                 pesan2 = 'basah'
#                 pesan1 = 'basah'
#                 time.sleep(10)

# if control == "ON":
#     print('Tanaman Sedang Di Siram')
# else:
#     print('Tanaman Basah')
# time.sleep(2)


