// SerialTest.ino
// This code tests serial communication between the pi and the arduino
//
// Written by Evan Brink

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

// The instructions
enum eInstruction
{
    I_Ping      = 1,
    I_Pour      = 2,
    I_Stop      = 3,
    I_Reverse   = 4,
};

// The responses
enum eResponse
{
    R_Success       = 0x01,
    R_Failure       = 0x02,
    R_CRCerror      = 0x03,
    R_PacketError   = 0x04,
};


// -------------------------------------------------
//                    MAIN CODE
// -------------------------------------------------

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

  // Initialize Serial communication
  Serial.begin(9600);
}

void loop() {
  // //wait until there's a message
  // if(Serial.available()){
  //   digitalWrite(DIRECTION, FW);
  //   delay(50);
  //   int bytesAvailable = Serial.available();
  //   byte inst[bytesAvailable];
  //   Serial.readBytes(inst, bytesAvailable);
  //
  //   if(inst[0] == 0xFF){
  //     digitalWrite(PUMP1,  HIGH);
  //   }
  //   else{
  //     digitalWrite(PUMP1,  LOW);
  //   }
  // }
  // digitalWrite(DIRECTION, BW);

  pumpThree(1, 1000, 2, 2000, 3, 3000,true);
  delay(1000);


  // digitalWrite(PUMP1,  HIGH);
  // digitalWrite(PUMP2,  HIGH);
  // digitalWrite(PUMP3,  HIGH);
  //
  // delay(1000);
  //
  // digitalWrite(PUMP1,  LOW);
  // digitalWrite(PUMP2,  LOW);
  // digitalWrite(PUMP3,  LOW);
  // delay(1000);

}

// -------------------------------------------------
//                HELPER FUNCTIONS
// -------------------------------------------------

// Helper function for pumping one ingredient
// p1 = pump number
// t1 = pump time in ms
// fw = true for pumping forward
void pumpOne(int p1, unsigned long t1, boolean fw){
  // set direction
  if(fw)
    digitalWrite(DIRECTION, FW);
  else
    digitalWrite(DIRECTION, BW);

  // start timer
  unsigned long st = millis();
  // start pumping
  startPump(p1);

  // wait until time is up
  boolean complete = false;
  while(!complete){
    if(millis() >= st + t1){
      complete = true;
      stopPump(p1);
    }
  }
  // TODO: Add response
}

// Helper function for pumping two ingredients
// p1 = first pump number
// t1 = first pump time in ms
// p2 = second pump number
// t2 = second pump time in ms
// fw = true for pumping forward
void pumpTwo(int p1,unsigned long t1,int p2,unsigned long t2,boolean fw){
  // set direction
  if(fw)
    digitalWrite(DIRECTION, FW);
  else
    digitalWrite(DIRECTION, BW);

  // start timer
  unsigned long st = millis();
  // start pumping
  startPump(p1);
  startPump(p2);

  // wait until time is up
  boolean complete1 = false;
  boolean complete2 = false;
  while(!(complete1 && complete2)){
    if(millis() >= st + t1){
      complete1 = true;
      stopPump(p1);
    }
    if(millis() >= st + t2){
      complete2 = true;
      stopPump(p2);
    }
  }
  // TODO: Add response
}


// Helper function for pumping three ingredients
// p1 = first pump number
// t1 = first pump time in ms
// p2 = second pump number
// t2 = second pump time in ms
// p3 = third pump number
// t3 = third pump time in ms
// fw = true for pumping forward
void pumpThree(int p1,unsigned long t1,int p2,unsigned long t2,int p3,
  unsigned long t3,boolean fw){
  // set direction
  if(fw)
    digitalWrite(DIRECTION, FW);
  else
    digitalWrite(DIRECTION, BW);

  // start timer
  unsigned long st = millis();
  // start pumping
  startPump(p1);
  startPump(p2);
  startPump(p3);

  // wait until time is up
  boolean complete1 = false;
  boolean complete2 = false;
  boolean complete3 = false;
  while(!(complete1 && complete2 && complete3)){
    if(millis() >= st + t1){
      complete1 = true;
      stopPump(p1);
    }
    if(millis() >= st + t2){
      complete2 = true;
      stopPump(p2);
    }
    if(millis() >= st + t3){
      complete3 = true;
      stopPump(p3);
    }
  }
  // TODO: Add response
}

// Helper function for pumping four ingredients
// p1 = first pump number
// t1 = first pump time in ms
// p2 = second pump number
// t2 = second pump time in ms
// p3 = third pump number
// t3 = third pump time in ms
// p4 = fourth pump number
// t4 = fourth pump time in ms
// fw = true for pumping forward
void pumpFour(int p1,unsigned long t1,int p2,unsigned long t2,int p3,
  unsigned long t3,int p4,unsigned long t4,boolean fw){
  // set direction
  if(fw)
    digitalWrite(DIRECTION, FW);
  else
    digitalWrite(DIRECTION, BW);

  // start timer
  unsigned long st = millis();
  // start pumping
  startPump(p1);
  startPump(p2);
  startPump(p3);
  startPump(p4);

  // wait until time is up
  boolean complete1 = false;
  boolean complete2 = false;
  boolean complete3 = false;
  boolean complete4 = false;
  while(!(complete1 && complete2 && complete3 && complete4)){
    if(millis() >= st + t1){
      complete1 = true;
      stopPump(p1);
    }
    if(millis() >= st + t2){
      complete2 = true;
      stopPump(p2);
    }
    if(millis() >= st + t3){
      complete3 = true;
      stopPump(p3);
    }
    if(millis() >= st + t4){
      complete4 = true;
      stopPump(p4);
    }
  }
  // TODO: Add response
}

// Helper function for starting pumps by number
void startPump(int pump){
  if(pump == 1)  digitalWrite(PUMP1,  HIGH);
  if(pump == 2)  digitalWrite(PUMP2,  HIGH);
  if(pump == 3)  digitalWrite(PUMP3,  HIGH);
  if(pump == 4)  digitalWrite(PUMP4,  HIGH);
  if(pump == 5)  digitalWrite(PUMP5,  HIGH);
  if(pump == 6)  digitalWrite(PUMP6,  HIGH);
  if(pump == 7)  digitalWrite(PUMP7,  HIGH);
  if(pump == 8)  digitalWrite(PUMP8,  HIGH);
  if(pump == 9)  digitalWrite(PUMP9,  HIGH);
  if(pump == 10) digitalWrite(PUMP10, HIGH);
  if(pump == 11) digitalWrite(PUMP11, HIGH);
  if(pump == 12) digitalWrite(PUMP12, HIGH);
}

// Helper function for stopping pumps by number
void stopPump(int pump){
  if(pump == 1)  digitalWrite(PUMP1,  LOW);
  if(pump == 2)  digitalWrite(PUMP2,  LOW);
  if(pump == 3)  digitalWrite(PUMP3,  LOW);
  if(pump == 4)  digitalWrite(PUMP4,  LOW);
  if(pump == 5)  digitalWrite(PUMP5,  LOW);
  if(pump == 6)  digitalWrite(PUMP6,  LOW);
  if(pump == 7)  digitalWrite(PUMP7,  LOW);
  if(pump == 8)  digitalWrite(PUMP8,  LOW);
  if(pump == 9)  digitalWrite(PUMP9,  LOW);
  if(pump == 10) digitalWrite(PUMP10, LOW);
  if(pump == 11) digitalWrite(PUMP11, LOW);
  if(pump == 12) digitalWrite(PUMP12, LOW);
}
