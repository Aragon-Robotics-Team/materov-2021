#define IN1 7;
#define IN2 6; 
#define ENA 9; //H-Bridge
//defining pins

//Note to self: calculate amount of time necessary for syringes to empty/fill up and put that into the necessary delays

void setup() {
  pinMode (IN1, OUTPUT);
  pinMode (IN2, OUTPUT);
  pinMode (ENA, OUTPUT);
  
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW); //can I put these two digitalWrites here?
  
  delay(1*60*1000); // delay for float to be put into appropriate spot
  sinkFloat();
  floatFloat();
  sinkFloat();
  floatFloat();
  analogWrite(ENA, 0);
  //float goes up last time and stops spinning
}

void sinkFloat() {
  delay(1*60*1000); //delay 2 mins to put into water. Can be changed later.
  //digitalWrite(IN1, HIGH); 
  //digitalWrite(IN2, LOW);
  analogWrite(ENA, 255); //check if this should be positive 255 or -255(we need the water to go INTO the syringes
  //maybe just use the digitalWrite high and low down below?
  //delay(how much ever time needed for the syringes to be full)
  //water uploaded; float will now sink
}

void floatFloat() {
  delay(1*60*1000); //now at seafloor
  //digitalWrite(IN1, LOW); //Do I need to turn on this motor again or will it be fine from before?
  //digitalWrite(IN2, HIGH); 
  analogWrite(ENA, -255);
  //syringes release water
  //delay(How much time it takes for syringes to empty);
}

//Figure out best pins on Arduino for easy installation and update code accordingly
// Use this link's diagram(for H-bridge pins): 
// https://www.bluetin.io/guides/l298n-h-bridge-dc-motor-driver-guide/attachment/l298n-dual-h-bridge-pin-connection-guide/
