// Template for Arduino Uno Projects
// Wokwi : https://wokwi.com/projects/
// ArduinoUNOblink : Wokwi project https://wokwi.com/projects/355889633279422465

#include <Arduino.h>

#define LED 13

void setup() 
{
  
  pinMode(LED, OUTPUT);

}

void loop() 
{

  digitalWrite(LED, HIGH);
  delay(200);
  digitalWrite(LED, LOW);
  delay(200);

}                                                                                