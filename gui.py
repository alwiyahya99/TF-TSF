from tkinter import *
import paho.mqtt.publish as publish
import time

root = Tk()
root.geometry('500x500')
root.title("GATEWAY CONFIGURATION")
var = IntVar()
c=StringVar()
ulang = False
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
        port.configure(state=NORMAL)
        topik.configure(state=DISABLED)
    elif event=="MQTT":
        host.configure(state=NORMAL)
        port.configure(state=NORMAL)
        topik.configure(state=NORMAL)
def kirim_mqtt():
    Topik = topik.get()
    Port = port.get()
    Host = host.get()
    publish.single(Topik, Port, hostname=Host)


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

submit=Button(root, text='Submit',width=20,bg='brown',fg='white', command=kirim_mqtt).place(x=180,y=400)

root.mainloop()