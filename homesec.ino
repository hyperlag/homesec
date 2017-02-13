/*
 * PIR sensor tester
 */
 
int input_pin1 = 2;               // Basement Sensor
int val = 0;                    // variable for reading the pin status
 
void setup() {
  pinMode(input_pin1, INPUT);     // declare sensor as input
 
  Serial.begin(9600);
}

int read_sensor(int pin){
  val = digitalRead(pin);  // read input value
  if (val == LOW) {    
    Serial.print("MOTION PIN: ");
    Serial.println(pin);
  } else {
    Serial.print("STILL PIN: ");
    Serial.println(pin);
  }
  return val;  
}

void loop(){
  read_sensor(input_pin1);
  delay(800);
}
