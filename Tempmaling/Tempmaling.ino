#include "max6675.h"

int thermoDO = 10;  // Dette er porten for data fra MAX6675
int thermoCS = 9;  // Dette er porten for CS signlet 
int thermoCLK = 11;  // Dette er porten for CLK signalet 

MAX6675 thermocouple(thermoCLK, thermoCS, thermoDO);


// 0 deg - 2.25
// 100 deg - 99.75, så snapper 


void setup() {
  Serial.begin(9600);
  Serial.println("MAX6675 test");
  // wait for MAX chip to stabilize
  delay(1000);
} 



void loop() {
  delay(5000);
  Serial.println(String(thermocouple.readCelsius()));  // Hvis tank 1 sender signal på logisk 1, skal temperaturen skrived med et 1. tall foran , 
}