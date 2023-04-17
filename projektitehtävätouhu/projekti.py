# Julkaistaan tietoa Thingspeakkiin MQTT avulla
# 
#
# CPU and RAM käyttö % ja CPU lämpötila lähetetään 15 sekunnin välein
# ThingSpeak kanavalle
#
# Importataan paho MQTT viestintää varten, psutil CPU ja RAM tietojen
# saantia varten, string merkkijonon käsittelyyn ja temp moduli 
# lämpötilatiedon hakemista varten
import paho.mqtt.publish as publish
import psutil
import string
import temp

# The ThingSpeak Channel ID.
# Replace <YOUR-CHANNEL-ID> with your channel ID.
channel_ID = "2011027"

# The hostname of the ThingSpeak MQTT broker.
# Säädä bool arvot haluamalle kommunikointitavalle True arvoksi
mqtt_host = "mqtt3.thingspeak.com"
useUnsecuredTCP=True
useUnsecuredWebsockets=False
useSSLWebsockets=False

# Thingspeak kirjautumistiedot
mqtt_client_ID = "GwILEQgYOTgwNDsfDCc2GCg"
mqtt_username  = "GwILEQgYOTgwNDsfDCc2GCg"
mqtt_password  = "y/EzLV4j+dhmSB/ImSaGTPCZ"

t_transport = "TCP"
t_port = 1883
# Create the topic string.
topic = "channels/" + channel_ID + "/publish"

while (True):

    # Haetaan tiedot 15 sekunnin välein
    cpu_percent = psutil.cpu_percent(interval=15)
    ram_percent = psutil.virtual_memory().percent
    cpu_temp = temp.get_cpu_temp()
    # Rakennetaan viesti
    payload = "field1=" + str(cpu_percent) + "&field2=" + str(ram_percent) + "&field3=" + str(cpu_temp)

    # attempt to publish this data to the topic.
    try:
       	print ("Writing Payload = ", payload," to host: ", mqtt_host, "clientID=2011027", mqtt_client_ID, mqtt_username, mqtt_password)
        publish.single(topic, payload, hostname=mqtt_host, transport=t_transport, port=t_port, client_id=mqtt_client_ID, auth={'username':mqtt_username,'password':mqtt_password})
    except (KeyboardInterrupt):
        break
    except Exception as e:
        print (e)

