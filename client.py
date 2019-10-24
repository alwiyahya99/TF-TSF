# import paho.mqtt.publish as publish
# import time
#
# pesan1 = "Basah"
# suhu = 3
# hum = 7
#
#
# while True:
#     # nilai = input('Masukan perintah : ')
#     a = str('{0},{1:0.1f},{2:0.1f}'.format(pesan1, suhu, hum))
#     publish.single("coeg/2", a, hostname="broker.hivemq.com")
#     print("Done")
#     suhu += 1
#     hum += 2
#     time.sleep(1)

from tkinter import *
#
# class RadioButton(Frame):
#     def __init__(self, parent):
#         Frame.__init__(self, parent)
#         self.window = parent
#         self.v = IntVar()
#
#         self.teks()
#         self.radioButton()
#
#     def teks(self):
#         Label(root, text="""pilih bahasa yang kalian sukai :""", justify=LEFT, padx=20).pack()
#
#     def radioButton(self):
#         Radiobutton(root, text="Indonesia", padx=20, command=self.tampilkan, variable=self.v, value=1).pack(anchor=W).place(x=235,y=130)
#         Radiobutton(root, text="Bahasa Inggris", padx=20, variable=self.v, command=self.tampilkan, value=2).pack(anchor=W)
#
#     def tampilkan(self):
#         if self.v.get() == 1:
#             print ("Bahasa Indonesia")
#         elif self.v.get() == 2:
#             print ("Bahasa inggris")
#
#
# if __name__ == '__main__':
#     root = Tk()
#     RadioButton(root)
#     mainloop()
#
#
from tkinter import *
import paho.mqtt.publish as publish
import time
import threading
import pymysql
import requests
# import serial

# arduino = serial.Serial("/dev/ttyACM0", 9600, timeout = 1)
# a = 1

# while True:
#     IN = arduino.readline()
#     try:
#         if IN != "":
#             IN2 = IN.split(","  )
#             kirim = [(IN[0], IN[1], IN[2], IN[3], IN[4], IN[5], IN[6], IN[7], IN[8], IN[9],
#                           IN[10], IN[11], IN[12], IN[13], IN[14], IN[15], IN[16], IN[17], IN[18], IN[19])]
#     except:
#         print("-------------")

root = Tk()
root.geometry('500x500')
root.title("GATEWAY CONFIGURATION")
var = IntVar()
kirim = 0
c=StringVar()
def select1():
    if var.get()==2:
        droplist.configure(state=NORMAL)
    elif var.get()==1:
        droplist.configure(state=DISABLED)
        c.set("TCP/IP")
        host.configure(state=NORMAL)
        port.configure(state=NORMAL)
        topik.configure(state=DISABLED)

def select2(event):
    event= c.get()
    if event=="TCP/IP":
        host.configure(state=NORMAL)
        port.configure(state=DISABLED)
        topik.configure(state=DISABLED)
    elif event=="MQTT":
        host.configure(state=NORMAL)
        port.configure(state=DISABLED)
        topik.configure(state=NORMAL)

def kirim():
    global kirim
    kirim =1
    run()
def stop():
    global kirim
    kirim =0
def run():
    def mengirim():
        Topik = topik.get()
        Port = port.get()
        Host = host.get()
        # IN = arduino.readline()
        IN = "10,11,12,13,14,15,1,1,1,1,1,1,1,1,1,1,1,1,1,1"
        # IN = arduino.readline()

        if var.get()==2:
            if c.get()=="MQTT":
                while kirim==1 :
                    if IN != "":
                        IN2 = IN.split(",")
                        kirim_data = [(IN2[0], IN2[1], IN2[2], IN2[3], IN2[4], IN2[5], IN2[6], IN2[7], IN2[8], IN2[9],
                                 IN2[10], IN2[11], IN2[12], IN2[13], IN2[14], IN2[15], IN2[16], IN2[17], IN2[18],
                                 IN2[19])]
                        # tampung=str(kirim_data)
                    # print(kirim_data)
                    publish.single(Topik, IN, hostname=host)
                    print("kirim")
                    if kirim==0:
                        print("stop")
                        break
            elif c.get()=="TCP/IP":
                temperature = 10
                humidity = 10
                pressure = 10

                print(temperature)
                print(humidity)
                print(pressure)

                while True:
                    temp = "%.1f" % temperature
                    hum = "%.1f" % humidity
                    press = "%.1f" % pressure
                    response = requests.post("http://"+Host+"/add_data.php?temp=" + temp + "&hum=" + hum + "&pr=" + press)
                    print(response.status_code)
                    print(response.text)
                    time.sleep(5)
                    if kirim==0:
                        print("stop")
                        break
        if var.get()==1:
            data = input('Masukan Data : ')
            con = pymysql.connect(db="gateway",
                                  user="root",
                                  passwd="",
                                  host=Host,
                                  port=int(Port))
            cursor = con.cursor()
            sql = "INSERT INTO Temperature " \
                  "SET Temperature = %s"

            val1 = [data]
            while kirim==1:

                # print data
                print(val1)
                cursor.executemany(sql, val1)
                con.commit()
                time.sleep(1)
                if kirim==0:
                    print("stop")
                    break
    thread = threading.Thread(target=mengirim)
    thread.start()


label_0 = Label(root, text="Gateway Configuration",width=20,font=("bold", 20))
label_0.place(x=100,y=53)

label_1 = Label(root, text="MODE :",width=20,font=("bold", 10))
label_1.place(x=85,y=130)

radio1 = Radiobutton(root, text="Intranet",padx = 5, variable=var, value=1, command = select1).place(x=235,y=130)
radio2 = Radiobutton(root, text="Internet", padx = 20, variable=var, value=2, command = select1).place(x=310,y=130)

label_2 = Label(root, text="PROTOKOL :",width=20,font=("bold", 10))
label_2.place(x=70,y=180)
list1 = ['TCP/IP', 'MQTT'];
droplist=OptionMenu(root,c, *list1, command=select2)
droplist.config(width=15,state=DISABLED)
droplist.grid(row=0, column=0)
c.set('Pilih Protokol')
droplist.place(x=240,y=180)

label_3 = Label(root, text="HOST :",width=20,font=("bold", 10))
label_3.place(x=87,y=230)
host = Entry(root,state=DISABLED)
host.place(x=240,y=230)

label_4 = Label(root, text="PORT :",width=20,font=("bold", 10))
label_4.place(x=87,y=280)
port = Entry(root,state=DISABLED)
port.place(x=240,y=280)

label_5 = Label(root, text="TOPIK :",width=20,font=("bold", 10))
label_5.place(x=85,y=330)
topik = Entry(root,state=DISABLED)
topik.place(x=240,y=330)

submit=Button(root, text='Kirim',width=20,bg='brown',fg='white', command=kirim).place(x=100,y=400)
stop=Button(root, text='Stop',width=20,bg='brown',fg='white', command=stop).place(x=280,y=400)

root.mainloop()