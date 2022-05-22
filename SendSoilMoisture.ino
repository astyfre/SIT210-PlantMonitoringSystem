const int soilPin = A1;

void setup() {
    
  Serial.begin(9600);
  pinMode(soilPin,INPUT);  
}

void loop() {
  
  int sensor_analog = analogRead(soilPin);
  float moisture_percent = (((sensor_analog/4095.00) * 100));
  Particle.publish("Plant_Moisture", String(moisture_percent));
  delay(3600000); //Checks once per hour
}
