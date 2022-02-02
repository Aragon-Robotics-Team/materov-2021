//https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0
#include <Servo.h> 
Servo servo;
Servo thruster;
//Servo thruster2;
int thruster1;
int thruster2;
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
  thruster.attach(10);
  thruster.writeMicroseconds(1500);
//  servo.write(90);
  angle = 0;
  var = 0;
}
  
void loop(){
  while (!Serial.available());
 
  thruster1 = Serial.readStringUntil(',').toInt();
  thruster2 = Serial.readStringUntil(',').toInt();
//  thruster3 = Serial.readStringUntil(',').toInt();
//  thruster4 = Serial.readStringUntil(',').toInt();
  
  sendValue = Serial.readStringUntil(',').toInt();
  servoopen = Serial.readStringUntil('\n').toInt();


//send to python

  Serial.println(
    String(thruster1) + "," 
  + String(thruster2) + "," 
  + String(sendValue) + "," 
  + String(servoopen)
  );

//thruster output
if(thruster1 < 1900 && thruster1 > 1100){
thruster.writeMicroseconds(thruster1);
}
  
//servo output
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


  
