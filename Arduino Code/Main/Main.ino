// Main.ino
// This code should be uploaded to the arduino. It handles communication with
// the pi and carries out instructions.

// define pins
#define DIRECTION A4
#define PUMP1     8
#define PUMP2     7
#define PUMP3     10 //Expected
#define PUMP4     9
#define PUMP5     2  //Expected
#define PUMP6     11 //Expected
#define PUMP7     A2
#define PUMP8     A3
#define PUMP9     4
#define PUMP10    3
#define PUMP11    6
#define PUMP12    5

#define FW        HIGH
#define BW        LOW


void setup() {
  // Set pins to output mode
  pinMode(DIRECTION,  OUTPUT);
  pinMode(PUMP1,      OUTPUT);
  pinMode(PUMP2,      OUTPUT);
  pinMode(PUMP3,      OUTPUT);
  pinMode(PUMP4,      OUTPUT);
  pinMode(PUMP5,      OUTPUT);
  pinMode(PUMP6,      OUTPUT);
  pinMode(PUMP7,      OUTPUT);
  pinMode(PUMP8,      OUTPUT);
  pinMode(PUMP9,      OUTPUT);
  pinMode(PUMP10,     OUTPUT);
  pinMode(PUMP11,     OUTPUT);
  pinMode(PUMP12,     OUTPUT);

  // Make sure all pumps are off
  digitalWrite(DIRECTION, FW);
  digitalWrite(PUMP1,  LOW);
  digitalWrite(PUMP2,  LOW);
  digitalWrite(PUMP3,  LOW);
  digitalWrite(PUMP4,  LOW);
  digitalWrite(PUMP5,  LOW);
  digitalWrite(PUMP6,  LOW);
  digitalWrite(PUMP7,  LOW);
  digitalWrite(PUMP8,  LOW);
  digitalWrite(PUMP9,  LOW);
  digitalWrite(PUMP10, LOW);
  digitalWrite(PUMP11, LOW);
  digitalWrite(PUMP12, LOW);

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
