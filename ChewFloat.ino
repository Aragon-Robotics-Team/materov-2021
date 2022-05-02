#include <Servo.h>

Servo myservo;  // create servo object to control a servo
const int servo = 9;
int val;    // variable to read the value from the analog pin

void delaySec(int s){
  for(int i=0; i<s; i++){
    delay(1000);
  }
} //delaying by the second

void sink(){
   myservo.write(0); //rubber is up
  delaySec(60);
}

void floaty(){
  myservo.write(180); //rubber is pulled in
  delaySec(60);
}


void setup() {
  myservo.attach(servo);  // attaches the servo on pin 9 to the servo object
  
}

void loop() {
  delaySec(60); //delay to put float into water(change to 3-5mins in competition)
  sink();
  floaty();
  sink();
  floaty();
  delay(60); //delay to go get float again
}
