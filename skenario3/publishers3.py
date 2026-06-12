import paho.mqtt.client as mqtt
import time
import random

BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPIK_CO2 = "airquality/room1/co2"
TOPIK_SUHU = "airquality/room1/temperature"
TOPIK_KELEMBABAN = "airquality/room1/humidity"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Publisher terhubung ke " + BROKER_HOST + ":" + str(BROKER_PORT))
        print("Topik: " + TOPIK_CO2 + ", " + TOPIK_SUHU + ", " + TOPIK_KELEMBABAN)
    else:
        print("Gagal terhubung, kode: " + str(rc))

def on_publish(client, userdata, mid):
    print("Pesan terkirim, id: " + str(mid))

client = mqtt.Client(client_id="publishers3")
client.on_connect = on_connect
client.on_publish = on_publish
client.connect(BROKER_HOST, BROKER_PORT, 60)
client.loop_start()

counter = 1
try:
    while True:
        co2 = random.randint(400, 1200)
        suhu = random.uniform(20.0, 35.0)
        kelembaban = random.uniform(40.0, 90.0)
        client.publish(TOPIK_CO2, "data ke " + str(counter) + ", CO2: " + str(co2) + " ppm")
        print("(Kirim) " + TOPIK_CO2 + ", CO2: " + str(co2) + " ppm")
        client.publish(TOPIK_SUHU, "data ke " + str(counter) + ", Suhu: " + str(round(suhu, 1)) + "C")
        print("(Kirim) " + TOPIK_SUHU + ", Suhu: " + str(round(suhu, 1)) + "C")
        client.publish(TOPIK_KELEMBABAN, "data ke " + str(counter) + ", Kelembaban: " + str(round(kelembaban, 1)) + "%")
        print("(Kirim) " + TOPIK_KELEMBABAN + ", Kelembaban: " + str(round(kelembaban, 1)) + "%")
        counter += 1
        time.sleep(3)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()