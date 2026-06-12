import paho.mqtt.client as mqtt
import time
import random

BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPIK_ROOM1_CO2 = "airquality/room1/co2"
TOPIK_ROOM1_SUHU = "airquality/room1/temperature"
TOPIK_ROOM1_KELEMBABAN = "airquality/room1/humidity"
TOPIK_ROOM2_CO2 = "airquality/room2/co2"
TOPIK_ROOM2_SUHU = "airquality/room2/temperature"
TOPIK_ROOM2_KELEMBABAN = "airquality/room2/humidity"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Publisher terhubung ke " + BROKER_HOST + ":" + str(BROKER_PORT))
    else:
        print("Gagal terhubung, kode: " + str(rc))

def on_publish(client, userdata, mid):
    print("Pesan terkirim, id: " + str(mid))

client = mqtt.Client(client_id="publishers5")
client.on_connect = on_connect
client.on_publish = on_publish
client.connect(BROKER_HOST, BROKER_PORT, 60)
client.loop_start()

counter = 1
try:
    while True:
        co2_r1 = random.randint(400, 1200)
        suhu_r1 = random.uniform(20.0, 35.0)
        kelembaban_r1 = random.uniform(40.0, 90.0)
        co2_r2 = random.randint(400, 1200)
        suhu_r2 = random.uniform(20.0, 35.0)
        kelembaban_r2 = random.uniform(40.0, 90.0)
        client.publish(TOPIK_ROOM1_CO2, "Data ke " + str(counter) + ", CO2: " + str(co2_r1) + " ppm")
        print("(Kirim) " + TOPIK_ROOM1_CO2 + ", CO2: " + str(co2_r1) + " ppm")
        client.publish(TOPIK_ROOM1_SUHU, "Data ke " + str(counter) + ", Suhu: " + str(round(suhu_r1, 1)) + " C")
        print("(Kirim) " + TOPIK_ROOM1_SUHU + ", Suhu: " + str(round(suhu_r1, 1)) + " C")
        client.publish(TOPIK_ROOM1_KELEMBABAN, "Data ke " + str(counter) + ", Kelembaban: " + str(round(kelembaban_r1, 1)) + " %")
        print("(Kirim) " + TOPIK_ROOM1_KELEMBABAN + ", Kelembaban: " + str(round(kelembaban_r1, 1)) + " %")
        client.publish(TOPIK_ROOM2_CO2, "Data ke " + str(counter) + ", CO2: " + str(co2_r2) + " ppm")
        print("(Kirim) " + TOPIK_ROOM2_CO2 + ", CO2: " + str(co2_r2) + " ppm")
        client.publish(TOPIK_ROOM2_SUHU, "Data ke " + str(counter) + ", Suhu: " + str(round(suhu_r2, 1)) + " C")
        print("(Kirim) " + TOPIK_ROOM2_SUHU + ", Suhu: " + str(round(suhu_r2, 1)) + " C")
        client.publish(TOPIK_ROOM2_KELEMBABAN, "Data ke " + str(counter) + ", Kelembaban: " + str(round(kelembaban_r2, 1)) + " %")
        print("(Kirim) " + TOPIK_ROOM2_KELEMBABAN + ", Kelembaban: " + str(round(kelembaban_r2, 1)) + " %")
        counter += 1
        time.sleep(3)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()