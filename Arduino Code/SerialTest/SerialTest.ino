// SerialTest.ino
// This code tests serial communication between the pi and the arduino
//
// Written by Evan Brink

// define pins
#define DIRECTION A4
#define PUMP1     6
#define PUMP2     5
#define PUMP3     4
#define PUMP4     3
#define PUMP5     A2
#define PUMP6     A3
#define PUMP7     2
#define PUMP8     11
#define PUMP9     8
#define PUMP10    7
#define PUMP11    10
#define PUMP12    9
#define LEDPIN    13

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
enum eStatus
{
    S_Success       = 0x01,
    S_Failure       = 0x02,
    S_CRCerror      = 0x03,
    S_PacketError   = 0x04,
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
  pinMode(LEDPIN,     OUTPUT);

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
  digitalWrite(LEDPIN, LOW);

  // Initialize Serial communication
  Serial.begin(9600);
}

void loop() {
  //wait until there's a message
  if(Serial.available()) {
    delay(30);
    // read instruction packet
    int bytesAvailable = Serial.available();
    byte inst[bytesAvailable];
    Serial.readBytes(inst, bytesAvailable);

    // TODO: Error Check
    // check for correct header and length
    boolean hdrCheck = (inst[0] == 0xFF);
    boolean lenCheck = (inst[1] == bytesAvailable - 2);

    // calculate CRC and compare
    int calculatedCRC = 0;
    int i = 1;
    while(i < bytesAvailable - 2) {
      calculatedCRC += inst[i];
      i++;
    }
    int recCRC = inst[bytesAvailable-2] + ((int)inst[bytesAvailable-1])*256;
    boolean crcCheck = (calculatedCRC == recCRC);

    byte instruction = inst[2];

    // if there's an error, return an error packet
    if(!(hdrCheck && lenCheck)) {
      sendResponse(instruction, S_PacketError);
    }
    if(!crcCheck) {
      sendResponse(instruction, S_CRCerror);
    }

    // if there's no error, carry out instructions
    if(crcCheck && hdrCheck && lenCheck) {
      // PING
      if(instruction == I_Ping) {
        ping();
        sendResponse(I_Ping, S_Success);
      }
      // STOP
      if(instruction == I_Stop) {
        stopAll();
        sendResponse(I_Stop, S_Success);
      }
      // POUR
      if(instruction == I_Pour) {
        boolean fw = true;
        // 1 ingredient
        if(bytesAvailable == 8) {
          int p1 = inst[3];
          unsigned long t1 = inst[4] + ((unsigned long) inst[5]) * 256;
          pumpOne(p1,t1,fw);
        }
        // 2 ingredients
        if(bytesAvailable == 11) {
          int p1 = inst[3];
          unsigned long t1 = inst[4] + ((unsigned long) inst[5]) * 256;
          int p2 = inst[6];
          unsigned long t2 = inst[7] + ((unsigned long) inst[8]) * 256;
          pumpTwo(p1,t1,p2,t2,fw);
        }
        // 3 ingredients
        if(bytesAvailable == 14) {
          int p1 = inst[3];
          unsigned long t1 = inst[4] + ((unsigned long) inst[5]) * 256;
          int p2 = inst[6];
          unsigned long t2 = inst[7] + ((unsigned long) inst[8]) * 256;
          int p3 = inst[9];
          unsigned long t3 = inst[10] + ((unsigned long) inst[11]) * 256;
          pumpThree(p1,t1,p2,t2,p3,t3,fw);
        }
        // 4 ingredients
        if(bytesAvailable == 17) {
          int p1 = inst[3];
          unsigned long t1 = inst[4] + ((unsigned long) inst[5]) * 256;
          int p2 = inst[6];
          unsigned long t2 = inst[7] + ((unsigned long) inst[8]) * 256;
          int p3 = inst[9];
          unsigned long t3 = inst[10] + ((unsigned long) inst[11]) * 256;
          int p4 = inst[12];
          unsigned long t4 = inst[13] + ((unsigned long) inst[14]) * 256;
          pumpFour(p1,t1,p2,t2,p3,t3,p4,t4,fw);
        }
        sendResponse(I_Pour, S_Success);
      }
      // REVERSE
      if(instruction == I_Reverse) {
        boolean fw = false;
        // 1 ingredient
        if(bytesAvailable == 8) {
          int p1 = inst[3];
          unsigned long t1 = inst[4] + ((unsigned long) inst[5]) * 256;
          pumpOne(p1,t1,fw);
        }
        // 2 ingredients
        if(bytesAvailable == 11) {
          int p1 = inst[3];
          unsigned long t1 = inst[4] + ((unsigned long) inst[5]) * 256;
          int p2 = inst[6];
          unsigned long t2 = inst[7] + ((unsigned long) inst[8]) * 256;
          pumpTwo(p1,t1,p2,t2,fw);
        }
        // 3 ingredients
        if(bytesAvailable == 14) {
          int p1 = inst[3];
          unsigned long t1 = inst[4] + ((unsigned long) inst[5]) * 256;
          int p2 = inst[6];
          unsigned long t2 = inst[7] + ((unsigned long) inst[8]) * 256;
          int p3 = inst[9];
          unsigned long t3 = inst[10] + ((unsigned long) inst[11]) * 256;
          pumpThree(p1,t1,p2,t2,p3,t3,fw);
        }
        // 4 ingredients
        if(bytesAvailable == 17) {
          int p1 = inst[3];
          unsigned long t1 = inst[4] + ((unsigned long) inst[5]) * 256;
          int p2 = inst[6];
          unsigned long t2 = inst[7] + ((unsigned long) inst[8]) * 256;
          int p3 = inst[9];
          unsigned long t3 = inst[10] + ((unsigned long) inst[11]) * 256;
          int p4 = inst[12];
          unsigned long t4 = inst[13] + ((unsigned long) inst[14]) * 256;
          pumpFour(p1,t1,p2,t2,p3,t3,p4,t4,fw);
        }
        sendResponse(I_Reverse, S_Success);
      }
    }
  }
}

// -------------------------------------------------
//                HELPER FUNCTIONS
// -------------------------------------------------

// Helper function for sending a response to the pi
// instruction = instruction that the pi sent previously
// status - chosen from eStatus according to success of task
void sendResponse(byte instruction, byte status) {
    byte u8_TxPacket[4];
    // -------- SEND INSTRUCTION ------------
    u8_TxPacket[0] = 0xFF;
    u8_TxPacket[1] = instruction;
    u8_TxPacket[2] = status;
    u8_TxPacket[3] = instruction + status; // CRC

    Serial.write(u8_TxPacket, 4);
    Serial.flush(); // waits until the last data byte has been sent
}

// helper fuction for ping - currently just flashes LED
void ping() {
  digitalWrite(LEDPIN, HIGH);
  delay(100);
  digitalWrite(LEDPIN, LOW);
}

// helper function for stopping all the pumps
void stopAll() {
  stopPump(1);
  stopPump(2);
  stopPump(3);
  stopPump(4);
  stopPump(5);
  stopPump(6);
  stopPump(7);
  stopPump(8);
  stopPump(9);
  stopPump(10);
  stopPump(11);
  stopPump(12);
}

// Helper function for pumping one ingredient
// p1 = pump number
// t1 = pump time in ms
// fw = true for pumping forward
void pumpOne(int p1, unsigned long t1, boolean fw) {
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
  while(!complete) {
    if(millis() >= st + t1) {
      complete = true;
      stopPump(p1);
    }
  }
}

// Helper function for pumping two ingredients
// p1 = first pump number
// t1 = first pump time in ms
// p2 = second pump number
// t2 = second pump time in ms
// fw = true for pumping forward
void pumpTwo(int p1,unsigned long t1,int p2,unsigned long t2,boolean fw) {
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
  while(!(complete1 && complete2)) {
    if(millis() >= st + t1) {
      complete1 = true;
      stopPump(p1);
    }
    if(millis() >= st + t2) {
      complete2 = true;
      stopPump(p2);
    }
  }
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
  unsigned long t3,boolean fw) {
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
  while(!(complete1 && complete2 && complete3)) {
    if(millis() >= st + t1) {
      complete1 = true;
      stopPump(p1);
    }
    if(millis() >= st + t2) {
      complete2 = true;
      stopPump(p2);
    }
    if(millis() >= st + t3) {
      complete3 = true;
      stopPump(p3);
    }
  }
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
  unsigned long t3,int p4,unsigned long t4,boolean fw) {
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
  while(!(complete1 && complete2 && complete3 && complete4)) {
    if(millis() >= st + t1) {
      complete1 = true;
      stopPump(p1);
    }
    if(millis() >= st + t2) {
      complete2 = true;
      stopPump(p2);
    }
    if(millis() >= st + t3) {
      complete3 = true;
      stopPump(p3);
    }
    if(millis() >= st + t4) {
      complete4 = true;
      stopPump(p4);
    }
  }
}

// Helper function for starting pumps by number
void startPump(int pump) {
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
void stopPump(int pump) {
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
