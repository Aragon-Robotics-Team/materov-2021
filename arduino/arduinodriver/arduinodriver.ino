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
  thruster1.attach(13); //thruster pins
  thruster2.attach(10);
  thruster3.attach(12);
  thruster4.attach(11);
  thruster1.writeMicroseconds(1500);
  thruster2.writeMicroseconds(1500);
  thruster3.writeMicroseconds(1500);
  thruster4.writeMicroseconds(1500);
  servo.write(90);
  angle = 90;
  delay(2000);
}

void loop(){
  while (!Serial.available());

  thruster1signal = Serial.readStringUntil(',').toInt();
  thruster2signal = Serial.readStringUntil(',').toInt();
  thruster3signal = Serial.readStringUntil(',').toInt();
  thruster4signal = Serial.readStringUntil(',').toInt();
  servoClose = Serial.readStringUntil(',').toInt();
  servoOpen = Serial.readStringUntil('.').toInt();

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
if(servo.read() > 5 && servoClose == 1){
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

//Serial.println("recieved");

  
//  Serial.println(
//    String(thruster1signal) + ","
//  + String(thruster2signal) + ","
//  + String(thruster3signal) + ","
//  + String(thruster4signal) + ","
//  + String(servoClose) + ","
//  + String(servoOpen));


delay(100);


}

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
}
