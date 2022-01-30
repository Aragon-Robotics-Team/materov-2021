//https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0

int thruster1;
int thruster2;
int thruster3;
int thruster4;

int servoclose;
int servoopen;

void setup(){
  Serial.begin(115200);
}
  
void loop(){
  while (!Serial.available());
  
  thruster1 = Serial.readStringUntil(',').toInt();
  thruster2 = Serial.readStringUntil(',').toInt();
//  thruster3 = Serial.readStringUntil(',').toInt();
//  thruster4 = Serial.readStringUntil(',').toInt();
  
  servoclose = Serial.readStringUntil(',').toInt();
  servoopen = Serial.readStringUntil('\n').toInt();


  Serial.println(
    String(thruster1) + "," 
  + String(thruster2) + "," 
  + String(servoclose) + "," 
  + String(servoopen)
  );

  //  + thruster3 + "," 
  //  + thruster4 + "," 
  
  }


  
