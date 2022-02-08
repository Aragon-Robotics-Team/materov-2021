//https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0
#include <Servo.h> 
Servo servo;
Servo thruster1;
Servo thruster2;
//Servo thruster2;
int thruster1signal;
int thruster2signal;
int thruster3;
int thruster4;

int sendValue;
int servoopen;

int servoVal;
int angle;
int var;
//int thruster;

void setup() {
  Serial.begin(115200);
  servo.attach(9);
  thruster1.attach(10);
  thruster2.attach(11);
  thruster1.writeMicroseconds(1500);
  thruster2.writeMicroseconds(1500);
  servo.write(90);
  angle = 90;
}
  
void loop(){
  while (!Serial.available());
 
  thruster1signal = Serial.readStringUntil(',').toInt();
  thruster2signal = Serial.readStringUntil(',').toInt();
//  thruster3 = Serial.readStringUntil(',').toInt();
//  thruster4 = Serial.readStringUntil(',').toInt();
  
  sendValue = Serial.readStringUntil(',').toInt();
  servoopen = Serial.readStringUntil('\n').toInt();


//send to python

  Serial.println(
    String(thruster1signal) + "," 
  + String(thruster2signal) + "," 
  + String(sendValue) + "," 
  + String(servoopen)
  );

//thruster output
if(thruster1signal < 1900 && thruster1signal > 1100){
thruster1.writeMicroseconds(thruster1signal);
}
if(thruster2signal < 1900 && thruster2signal > 1100){
thruster2.writeMicroseconds(thruster2signal);
}
  
//servo output
if(servo.read() > 5 && sendValue == 1){
  angle = angle - 5;
  servo.write(angle);
  }
if(servo.read() <  175 && servoopen ==1){
  angle = angle + 5;
  servo.write(angle);
  }
//
//  if(sendValue == 1){
//      if (servo.read()> 0 && servo.read()<= 175){
//        angle = angle + 5;
//      }
//      if (servo.read()==180){
//        var = angle - 180;
//        angle = var + 5;
//      }
//      servo.write(angle);
//      //delay(100);
//  }
//    if(sendValue == 60){
//      angle = angle + 0;
//    }
  
  }


  
