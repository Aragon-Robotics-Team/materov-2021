//https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0
#include <Servo.h>
Servo servo;
Servo thruster1;
Servo thruster2;
Servo thruster3;
Servo thruster4;

int laserPin = 8;

int thruster1signal;
int thruster2signal;
int thruster3signal;
int thruster4signal;

int servoClose;
int servoOpen;

int servoVal;
int angle;
int var;

void setup() {
  Serial.begin(115200);
  servo.attach(9); //servo pin
  pinMode(laserPin, OUTPUT);
  thruster1.attach(10); //thruster pins
  thruster2.attach(11);
  thruster3.attach(12);
  thruster4.attach(13);
  thruster1.writeMicroseconds(1500);
  thruster2.writeMicroseconds(1500);
  thruster3.writeMicroseconds(1500);
  thruster4.writeMicroseconds(1500);
  delay(2000);
}

void loop(){
  thruster1.writeMicroseconds(1500);
  thruster2.writeMicroseconds(1500);
  thruster3.writeMicroseconds(1500);
  thruster4.writeMicroseconds(1500);
  delay(200)
}