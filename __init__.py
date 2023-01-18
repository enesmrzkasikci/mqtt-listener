from paho.mqtt.client import Client

def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    derece = int(message.payload)
    if derece > 35:
        print("klimayı aç")

    if derece < 10:
        print("kaloriferi aç")


client = Client("eness")
client.connect("localhost")
client.subscribe("oda")

client.on_message = on_message
client.loop_forever()



