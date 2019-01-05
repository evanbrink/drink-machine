#define DIRECTION A4
#define PUMP1 A3
#define PUMP2 A3
#define FW    HIGH
#define BW    LOW

void setup() {
  // put your setup code here, to run once:
  pinMode(DIRECTION,  OUTPUT);
  pinMode(PUMP1,      OUTPUT);
  pinMode(PUMP2,      OUTPUT);
}

void loop() {
  // Forward on
  digitalWrite(DIRECTION, FW);
  digitalWrite(PUMP2, HIGH);
  delay(1000);
  // Forward off
  digitalWrite(PUMP2, LOW);
  delay(1000);
  // Reverse on
  digitalWrite(DIRECTION, BW);
  digitalWrite(PUMP2, HIGH);
  delay(1000);
  // Reverse off
  digitalWrite(PUMP2, LOW);
  delay(1000);
  
}
