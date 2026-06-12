import paho.mqtt.client as mqtt

BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPIK_WILDCARD = "airquality/#"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Subscriber terhubung ke " + BROKER_HOST + ":" + str(BROKER_PORT))
        print("Subscribe ke topik: " + TOPIK_WILDCARD)
        client.subscribe(TOPIK_WILDCARD)
    else:
        print("Gagal terhubung, kode: " + str(rc))

def on_message(client, userdata, msg):
    print("(Terima) " + msg.topic + ": " + msg.payload.decode("utf-8"))

client = mqtt.Client(client_id="subscribers5")
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER_HOST, BROKER_PORT, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    client.disconnect()