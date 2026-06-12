import paho.mqtt.client as mqtt

BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPIK_CO2 = "airquality/room1/co2"
TOPIK_SUHU = "airquality/room1/temperature"
TOPIK_KELEMBABAN = "airquality/room1/humidity"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Subscriber terhubung ke " + BROKER_HOST + ":" + str(BROKER_PORT))
        client.subscribe(TOPIK_CO2)
        print("Subscribe ke topik: " + TOPIK_CO2)
        client.subscribe(TOPIK_SUHU)
        print("Subscribe ke topik: " + TOPIK_SUHU)
        client.subscribe(TOPIK_KELEMBABAN)
        print("Subscribe ke topik: " + TOPIK_KELEMBABAN)
    else:
        print("Gagal terhubung, kode: " + str(rc))

def on_message(client, userdata, msg):
    print("(Terima) " + msg.topic + ": " + msg.payload.decode("utf-8"))

client = mqtt.Client(client_id="subscribers3")
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER_HOST, BROKER_PORT, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    client.disconnect()