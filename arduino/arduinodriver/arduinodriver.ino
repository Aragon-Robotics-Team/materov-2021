//https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0
#include <Servo.h> 
Servo servo;
Servo thruster1;
Servo thruster2;
Servo thruster3;
Servo thruster4;

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
}

void loop(){
  while (!Serial.available());

  thruster1signal = Serial.readStringUntil(',').toInt();
  thruster2signal = Serial.readStringUntil(',').toInt();
  thruster3signal = Serial.readStringUntil(',').toInt();
  thruster4signal = Serial.readStringUntil(',').toInt();
  servoClose = Serial.readStringUntil(',').toInt();
  servoOpen = Serial.readStringUntil(',').toInt();

//thruster output
if(thruster1signal > 1900 || thruster1signal < 1100){
thruster1signal = 1500;
}
if(thruster2signal > 1900 || thruster2signal < 1100){
thruster2signal = 1500;
}
if(thruster3signal > 1900 || thruster3signal < 1100){
thruster3signal = 1500;
}
if(thruster4signal > 1900 || thruster4signal < 1100){
thruster4signal = 1500;
}

//servo output
if(servo.read() > 5 && servoOpen == 1){
  angle = angle - 5;
  }
else if(servo.read() <  175 && servoOpen == 1){
  angle = angle + 5;
  }

servo.write(angle);
thruster1.writeMicroseconds(thruster1signal);
thruster2.writeMicroseconds(thruster2signal);
thruster3.writeMicroseconds(thruster3signal);
thruster4.writeMicroseconds(thruster4signal);

delay((1/50) * 1000);


}


  
//  Serial.println(
//    String(thruster1signal) + ","
//  + String(thruster2signal) + ","
//  + String(thruster3signal) + ","
//  + String(thruster4signal) + ","
//  + String(servoClose) + ","
//  + String(servoOpen));
//
