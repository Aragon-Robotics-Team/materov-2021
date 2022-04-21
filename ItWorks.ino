const int IN3 = 7;
const int IN4 = 6;


void delayMin(int m){
  for(int i =0; i<10*m; i++){
    delay(1000);
  }
} //delaying by the minute

void delaySec(int s){
  for(int i=0; i<10*s; i++){
    delay(1000);
  }
} //delaying by the second


void sinkFloat(){
  digitalWrite(IN1, HIGH); //5V
  digitalWrite(IN2, LOW); //Ground
  delaySec(20); //delay 20 sec
    //water uploaded; float will now sink
  
}

void floatFloat(){
  digitalWrite(IN1, LOW); //5V
  digitalWrite(IN2, HIGH);
  delaySec(20);
}

//NTS: Calculate amount of time necessary for syringes to empty/fill up
//Found to be 20 seconds

void setup() {
  pinMode (IN1, OUTPUT);
  pinMode (IN2, OUTPUT);
  //Arduino controls every pin(no input pins)
}

void loop() {
  // MOTOR GOES LEFT FIRST AND THEN RIGHT. Change as needed.
  
  //delayMin(5);  <-- So float can be deployed before starting buoyancy gimmicks
  sinkFloat();
  delayMin(1);
  floatFloat();
  delayMin(1);
  sinkFloat();
  delayMin(1);
  floatFloat();
  delayMin(1);
  
  //delayMin(10);  <-- So float can be retrieved with no buoyancy gimmicks
}

//At testing check: If buoyancy time is enough(for it to sink and then float back up)
