#include <Servo.h>
Servo sg90;
int gelenveriint;
#define ledPin 10

void setup() {
  Serial.begin(9600);
  sg90.attach(9);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    gelenveriint = Serial.parseInt();  
    if (gelenveriint >= 0 && gelenveriint <= 180) { 
      sg90.write(gelenveriint);
      
      int ledBrightness = map(gelenveriint, 0, 180, 0, 255); 
      analogWrite(ledPin, ledBrightness);
      
      delay(10);
    }
  }
}
