const int soilPin = A4;

void setup() {
  Serial.begin(9600);

}

void loop() {
  
  int sensor_analog = analogRead(soilPin);
  float moisture_percent = (100 - ((sensor_analog/4095.00) * 100));
  
  String Soil_Moisture = String(soilPin);
  Serial.print("Moisture percent");
  Serial.print(moisture_percent);
  Particle.publish("Plant_Moisture", Soil_Moisture);
  delay(5000000);

}


