#include <Arduino.h>

#define LED 13

void setup() 
{
  
  pinMode(LED, OUTPUT);

}

void loop() 
{
// modified on chromebook
  digitalWrite(LED, HIGH);
  delay(1500);
  digitalWrite(LED, LOW);
  delay(200);

}                                                                                