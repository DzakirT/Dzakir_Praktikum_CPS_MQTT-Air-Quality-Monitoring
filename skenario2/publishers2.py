import paho.mqtt.client as mqtt
import time
import random

BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPIC = "airquality/room1/co2"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Publisher terhubung ke " + BROKER_HOST + ":" + str(BROKER_PORT))
        print("Topik: " + TOPIC)
    else:
        print("Gagal terhubung, kode: " + str(rc))

def on_publish(client, userdata, mid):
    print("Pesan terkirim, id: " + str(mid))

client = mqtt.Client(client_id="publishers2")
client.on_connect = on_connect
client.on_publish = on_publish
client.connect(BROKER_HOST, BROKER_PORT, 60)
client.loop_start()

counter = 1
try:
    while True:
        co2 = random.randint(400, 1200)
        for qos in [0, 1, 2]:
            pesan = "data ke " + str(counter) + ", CO2: " + str(co2) + " ppm, QoS: " + str(qos)
            client.publish(TOPIC, pesan, qos=qos)
            print("(Kirim) QoS " + str(qos) + ", " + pesan)
            time.sleep(1)
        counter += 1
        time.sleep(2)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()