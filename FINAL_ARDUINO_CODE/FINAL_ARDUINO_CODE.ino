#include <Wire.h>
#include "pitches.h"
#define soundPin 5 // speaker pin
int mpu = 0x68;//I2C address of the MPU-6050
int16_t AcX, AcY, AcZ;
int data;
unsigned long endTime;
unsigned long int startTime;
int maximum;
int minimum;
bool freeze[] = {0,0};
int counter = -1;
bool checkAlarm = false;
bool ringAlarm = false;
   
void setup() {
  // put your setup code here, to run once:AK
  Wire.begin();
  Wire.beginTransmission(mpu);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  Wire.beginTransmission(mpu);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(mpu, 14, true);
  maximum = -10000;
  minimum = 10000;
  startTime = millis();
  AcX = Wire.read() <<8| Wire.read();
  AcY = Wire.read() <<8| Wire.read();
  AcZ = Wire.read() <<8| Wire.read();
  endTime = startTime + 1000;
  while (startTime < endTime)
  {
    //Serial.println(AcZ);
    Wire.beginTransmission(mpu);
    Wire.write(0x3B);
    Wire.endTransmission(false);
    Wire.requestFrom(mpu, 14, true);
    AcX = Wire.read() <<8| Wire.read();
    AcY = Wire.read() <<8| Wire.read();
    AcZ = Wire.read() <<8| Wire.read();
    if (maximum < AcZ)
      {
        maximum = AcZ;
      }
    if (minimum > AcZ)
     {
      minimum = AcZ;
     }
     startTime = millis();
  }
  counter = counter + 1;
  Serial.print ("Seconds gone by: ");
  Serial.println(counter);
  Serial.print("maximum: ");
  Serial.println(maximum);
  if (maximum < 5000 && maximum > -1500)
  {
    freeze[counter%2] = 1;
    Serial.print("maximum value is: ");
    Serial.println(maximum);
    Serial.print("the counter is: ");
    Serial.println(counter%2);
  }
  else
  {
    freeze[counter%2] = 0;
  }

  for (int i = 0; i < 2; i++)
  {
    if (freeze[i] == 0)
    {
      checkAlarm = false;
      break;
    }
    else
    {
      checkAlarm = true;
    }
  }

  if (checkAlarm == true)
  {
    Wire.beginTransmission(mpu);
    Wire.write(0x3B);
    Wire.endTransmission(false);
    Wire.requestFrom(mpu, 14, true);
    AcX = Wire.read() <<8| Wire.read();
    AcY = Wire.read() <<8| Wire.read();
    AcZ = Wire.read() <<8| Wire.read();
    while (AcZ < 5500 && AcZ >  -5500)
    {
      Wire.beginTransmission(mpu);
      Wire.write(0x3B);
      Wire.endTransmission(false);
      Wire.requestFrom(mpu, 14, true);
      AcX = Wire.read() <<8| Wire.read();
      AcY = Wire.read() <<8| Wire.read();
      AcZ = Wire.read() <<8| Wire.read();
      Serial.println(AcZ);
      tone(soundPin, NOTE_A4, 50);
      delay(900);
      tone(soundPin, NOTE_E4, 50);
      delay(900);
   
    }
  }
  checkAlarm = false;
}
