# SIT210-PlantMonitoringSystem
SIT210 Final Project
Uses a Raspberry Pi and a Particle Argon.

**DEVICE COMMUNICATION**
To get the devices to commuinicate I have used webhooks.
Firstly create a new channel on thingspeak.com
Set the field1 to Plant_Moisture.
Copy your unique API Write Key 

Then create a new webhook integration on Particle.
set Event name to Plant_Moisture, URL to https://api.thingspeak.com/update and request type to POST.
Go to advanced settings change form field to custom and put the first row as 'api_key' > _your_API_key_
in the second row put 'field1' > '{{{PARTICLE_EVENT_VALUE}}}'

Now you should be able to send data to thingspeak from particle using 'Particle.publish("Plant_Moisture", Soil_Moisture);' 

From the RaspberryPi's end there is a function 'def read_data_thingspeak' that will read the data that was published to thingspeak. 
