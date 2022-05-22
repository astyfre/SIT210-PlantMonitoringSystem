# SIT210-PlantMonitoringSystem
SIT210 Final Project
Uses:
Raspberry Pi, Particle Argon, DFRobot Soil Moisture Sensor V2, 3mm LEDs', resistor


**DEVICE COMMUNICATION**
To get the devices to commuinicate I have used webhooks.
Firstly create a new channel on https://thingspeak.com
Set the field1 to Plant_Moisture.
Copy your unique API Write Key 

Then create a new webhook integration on Particle.
set Event name to Plant_Moisture, URL to https://api.thingspeak.com/update and request type to POST.
Go to advanced settings change form field to custom and put the first row as 'api_key' > _your_API_key_
in the second row put 'field1' > '{{{PARTICLE_EVENT_VALUE}}}'

Now you should be able to send data to thingspeak from particle using 'Particle.publish("Plant_Moisture", Soil_Moisture);' 

From the RaspberryPi's end there is a function 'def read_data_thingspeak' that will read the data that was published to thingspeak. 
The URL will be https://api.thingspeak.com/channels/_YOURCHANNELID_/fields/1.json?api_key=
and the KEY will be your API Read Key found in the 'API Keys' setting
!!For help with how to format this go to https://au.mathworks.com/help/thingspeak/readfield.html

Link to project Video: 
