//https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0
#include <Servo.h>
Servo servo;
Servo thruster1;
Servo thruster2;
Servo thruster3;
Servo thruster4;

int laserPin = 7;
int laserStatus = 0;

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
  digitalWrite(laserPin, LOW);
  thruster1.attach(10); //thruster pins
  thruster2.attach(11);
  thruster3.attach(12);
  thruster4.attach(13);
  thruster1.writeMicroseconds(1500);
  thruster2.writeMicroseconds(1500);
  thruster3.writeMicroseconds(1500);
  thruster4.writeMicroseconds(1500);
  servo.write(90);
  angle = 90;
  delay(2000);
}

void loop() {
  while (!Serial.available());

  thruster1signal = Serial.readStringUntil(',').toInt();
  thruster2signal = Serial.readStringUntil(',').toInt();
  thruster3signal = Serial.readStringUntil(',').toInt();
  thruster4signal = Serial.readStringUntil(',').toInt();
  servoClose = Serial.readStringUntil(',').toInt();
  servoOpen = Serial.readStringUntil(',').toInt();
  laserStatus = Serial.readStringUntil('.').toInt();


  //thruster output
  if (thruster1signal > 1740) {
    thruster1signal = 1740;
  }
  if (thruster1signal < 1260) {
    thruster1signal = 1260;
  }
  if (thruster2signal > 1740) {
    thruster2signal = 1740;
  }
  if (thruster2signal < 1260) {
    thruster2signal = 1260;
  }
  if (thruster3signal > 1740) {
    thruster3signal = 1740;
  }
  if (thruster3signal < 1260) {
    thruster3signal = 1260;
  }
  if (thruster4signal > 1740) {
    thruster4signal = 1740;
  }
  if (thruster4signal < 1260) {
    thruster4signal = 1260;
  }

  //servo output
  if (servo.read() > 5 && servoClose == 1) {
    angle = angle - 5;
  }
  else if (servo.read() <  175 && servoOpen == 1) {
    angle = angle + 5;
  }

  servo.write(angle);
  thruster1.writeMicroseconds(thruster1signal);
  thruster2.writeMicroseconds(thruster2signal);
  thruster3.writeMicroseconds(thruster3signal);
  thruster4.writeMicroseconds(thruster4signal);

  digitalWrite(laserPin, laserStatus);

  //Serial.println("recieved");

  Serial.println(
    String(thruster1signal) + ","
    + String(thruster2signal) + ","
    + String(thruster3signal) + ","
    + String(thruster4signal) + ","
    + String(servoClose) + ","
    + String(servoOpen) + ","
    + String(laserStatus) + ",");



  delay(100);


}
