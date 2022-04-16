#define IN1 7;
#define IN2 6; 
#define ENA 9; //H-Bridge
//defining pins

int t = 1*60*1000;

//Note to self: calculate amount of time necessary for syringes to empty/fill up and put that into the necessary delays: Found to be 20 seconds

void setup() {
  pinMode (IN1, OUTPUT);
  pinMode (IN2, OUTPUT);
  pinMode (ENA, OUTPUT);
  //Arduino controls every pin(no input pins)
  
  digitalWrite(IN1, HIGH); //5V
  digitalWrite(IN2, LOW); //Ground
  
  delay(3*60*1000); // delay for float to be put into appropriate spot(setup+carrying to product demo area)
  
  sinkFloat();
  delay(t);
  floatFloat();
  delay(t);
  sinkFloat();
  delay(t);
  floatFloat();
  delay(t);
  analogWrite(ENA, 0);
  //float goes up last time and stops spinning
}

void sinkFloat(){
  analogWrite(ENA, 255); //check if this should be positive 255 or -255(we need the water to go INTO the syringes
  delay(1*20*1000); //delay 20 sec
    //water uploaded; float will now sink
}

void floatFloat(){
  analogWrite(ENA, -255);
  //syringes release water
   delay(1*20*1000);
}

//Figure out best pins on Arduino for easy installation and update code accordingly
// Use this link's diagram(for H-bridge pins): 
// https://www.bluetin.io/guides/l298n-h-bridge-dc-motor-driver-guide/attachment/l298n-dual-h-bridge-pin-connection-guide/
