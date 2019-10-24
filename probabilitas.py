# import sys
# from Adafruit_IO import MQTTClient
#
# ADAFRUIT_IO_KEY = '205ed22f84a64ee088e8d718e59e0e9f'
# ADAFRUIT_IO_USERNAME = 'alwiyahya99'
# FEED_ID = 'onoff'
#
# def connected(client):
#     print('Connected to Adafruit IO!  Listening for {0} changes...'.format(FEED_ID))
#     client.subscribe(FEED_ID)
#
# def disconnected(client):
#     print('Disconnected from Adafruit IO!')
#     sys.exit(1)
#
# def message(client, feed_id, payload):
#     print('Feed {0} received new value: {1}'.format(feed_id, payload))
#
# client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
#
# client.on_connect    = connected
# client.on_disconnect = disconnected
# client.on_message    = message
#
# client.connect()
# client.loop_blocking()
#

while True:
    a = input('Masukan Nilai : ')

    if int(a) >= 80:
        print('index nilai A')
    elif int(a) >= 69:
        print('index nilai B')
    elif int(a) >= 49:
        print('index nilai C')
    else:
        print('index nilai D')