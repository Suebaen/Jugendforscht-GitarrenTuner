#include <Arduino.h>
#include <SoftwareSerial.h>


// Motor für das G
int MotorG_R = 2;
int MotorG_L = 3;

// Motor für das F
int MotorF_R = 4;
int MotorF_L = 5;

// Motor für das A
int MotorA_L = 6;
int MotorA_R = 7;

// Motor für das C
int MotorC_L = 8;
int MotorC_R = 9;

// Motor für das D
int MotorD_R = 10;
int MotorD_L = 11;

// Motor für das E
int MotorE_R = 12;
int MotorE_L = 13;


SoftwareSerial serial_connection(0, 1);
#define BUFFER_SIZE 64
const int stepsPerRevolution = 50;
char inData[BUFFER_SIZE];
char inChar=-1;
int count=0;
int i = 0;
int winkel = 90;
int warten = 100;
int UmWievielSichDerServoDrehenSOll = 200;
int first_bytes;
int remainf_bytes=0;
byte byte_count;
int stepCount = 0; 
int steps = 3;

void setup() {
  Serial.begin(9600);
  serial_connection.begin(9600);
  serial_connection.println("Ready!!");
  Serial.println("Started");
  }

void loop() {
    byte_count=serial_connection.available();


    if (byte_count){
      Serial.println("Incoming Data");
      first_bytes=byte_count;
      remainf_bytes=0;
      if (first_bytes>=BUFFER_SIZE-1){
        remainf_bytes=byte_count-(BUFFER_SIZE-1);
      }
      
      for (i = 0; i < first_bytes; i++){
        inChar=serial_connection.read();
        inData[i]=inChar;
       Serial.println(first_bytes); 
      }
      inData[i]='\0';
        
      // Motor für das F
      if (String(inData)=="N"){
        Serial.println(inData);
        digitalWrite(MotorF_R, HIGH);
        digitalWrite(MotorF_L, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

      if (String(inData)=="NNN"){
        Serial.println(inData);
      digitalWrite(MotorF_R, HIGH);
        digitalWrite(MotorF_L, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

      if (String(inData)=="NNNN"){
        Serial.println(inData);
      digitalWrite(MotorF_R, HIGH);
        digitalWrite(MotorF_L, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

      if (String(inData)=="FN"){
        Serial.println(inData);
      digitalWrite(MotorF_R, HIGH);
        digitalWrite(MotorF_L, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

      if (String(inData)=="NFN"){
        Serial.println(inData);
      digitalWrite(MotorF_R, HIGH);
        digitalWrite(MotorF_L, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

      if (String(inData)=="NNNNNN"){
        Serial.println(inData);
      digitalWrite(MotorF_R, HIGH);
        digitalWrite(MotorF_L, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

      if (String(inData)=="F"){
        Serial.println(inData);
        digitalWrite(MotorF_R, LOW);
        digitalWrite(MotorF_L, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 
      
      if (String(inData)=="FF"){
        digitalWrite(MotorF_R, LOW);
        digitalWrite(MotorF_L, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 

      if (String(inData)=="FFF"){
        digitalWrite(MotorF_R, LOW);
        digitalWrite(MotorF_L, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 

      // Motor für das A
      if (String(inData)=="A"){
        Serial.println(inData);
        digitalWrite(MotorA_L, HIGH);
        digitalWrite(MotorA_R, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

      if (String(inData)=="AA"){
        Serial.println(inData);
        digitalWrite(MotorA_L, HIGH);
        digitalWrite(MotorA_R, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

      if (String(inData)=="ABA"){
        Serial.println(inData);
        digitalWrite(MotorA_L, HIGH);
        digitalWrite(MotorA_R, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

      if (String(inData)=="AAA"){
        Serial.println(inData);
        digitalWrite(MotorA_L, HIGH);
        digitalWrite(MotorA_R, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

      if (String(inData)=="AAAAAAA"){
        Serial.println(inData);
        digitalWrite(MotorA_L, HIGH);
        digitalWrite(MotorA_R, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

      if (String(inData)=="B"){
        Serial.println(inData);
        digitalWrite(MotorA_L, LOW);
        digitalWrite(MotorA_R, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 
      
      if (String(inData)=="BB"){
        digitalWrite(MotorA_L, LOW);
        digitalWrite(MotorA_R, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 

      if (String(inData)=="BBB"){
        digitalWrite(MotorA_L, LOW);
        digitalWrite(MotorA_R, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      }

      if (String(inData)=="BBBB"){
        digitalWrite(MotorA_L, LOW);
        digitalWrite(MotorA_R, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 


      // Motor für das C
      if (String(inData)=="C"){
        Serial.println(inData);
      digitalWrite(MotorF_R, HIGH);
        digitalWrite(MotorF_L, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

      if (String(inData)=="CC"){
        Serial.println(inData);
        digitalWrite(MotorF_R, HIGH);
        digitalWrite(MotorF_L, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

      if (String(inData)=="CCC"){
        Serial.println(inData);
        digitalWrite(MotorF_R, HIGH);
        digitalWrite(MotorF_L, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

      if (String(inData)=="CCCC"){
        Serial.println(inData);
        digitalWrite(MotorF_R, HIGH);
        digitalWrite(MotorF_L, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

      if (String(inData)=="L"){
        Serial.println(inData);
        digitalWrite(MotorF_R, LOW);
        digitalWrite(MotorF_L, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 
      
      if (String(inData)=="LL"){
        digitalWrite(MotorF_R, LOW);
        digitalWrite(MotorF_L, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 

      if (String(inData)=="LLL"){
        digitalWrite(MotorF_R, LOW);
        digitalWrite(MotorF_L, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 

      if (String(inData)=="LLLL"){
        digitalWrite(MotorF_R, LOW);
        digitalWrite(MotorF_L, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 
      
      //Motor für das G 
      if (String(inData)=="G"){
        digitalWrite(MotorG_R, HIGH);
        digitalWrite(MotorG_L, LOW);
        Serial.print("steps:");
        delay(warten);
      }

      if (String(inData)=="GG"){
        digitalWrite(MotorG_R, HIGH);
        digitalWrite(MotorG_L, LOW);
        Serial.print("steps:");
        delay(warten);
      }

      if (String(inData)=="GGG"){
        digitalWrite(MotorG_R, HIGH);
        digitalWrite(MotorG_L, LOW);
        Serial.print("steps:");
        delay(warten);
      }

      if (String(inData)=="GGGG"){
        digitalWrite(MotorG_R, HIGH);
        digitalWrite(MotorG_L, LOW);
        Serial.print("steps:");
        delay(warten);
      }

      if (String(inData)=="K"){
        digitalWrite(MotorG_R, LOW);
        digitalWrite(MotorG_L, HIGH);
        Serial.print("steps:");
        delay(warten);
      }

      if (String(inData)=="KK"){
        digitalWrite(MotorG_R, LOW);
        digitalWrite(MotorG_L, HIGH);
        Serial.print("steps:");
        delay(warten);
      }

      if (String(inData)=="KKK"){ //das KKK steht NICHT for den Ku-Klux-Klan
        digitalWrite(MotorG_R, LOW);
        digitalWrite(MotorG_L, HIGH);
        Serial.print("steps:");
        delay(warten);
      }

      if (String(inData)=="KKKK"){
        digitalWrite(MotorG_R, LOW);
        digitalWrite(MotorG_L, HIGH);
        Serial.print("steps:");
        delay(warten);
      }

      //Motor für das E
      if(String(inData)=="E"){
        digitalWrite(MotorE_R, HIGH);
        digitalWrite(MotorE_L, LOW);
        Serial.print("steps:");
        delay(warten);
      }

      if(String(inData)=="EE"){
        digitalWrite(MotorE_R, HIGH);
        digitalWrite(MotorE_L, LOW);
        Serial.print("steps:");
        delay(warten);
      }

      if(String(inData)=="EEE"){
        digitalWrite(MotorE_R, HIGH);
        digitalWrite(MotorE_L, LOW);
        Serial.print("steps:");
        delay(warten);
      }

      if(String(inData)=="EEEE"){
        digitalWrite(MotorE_R, HIGH);
        digitalWrite(MotorE_L, LOW);
        Serial.print("steps:");
        delay(warten);
      }

      if(String(inData)=="Q"){
        digitalWrite(MotorE_R, LOW);
        digitalWrite(MotorE_L, HIGH);
        Serial.print("steps:");
        delay(warten);
      }

      if(String(inData)=="QQ"){
        digitalWrite(MotorE_R, LOW);
        digitalWrite(MotorE_L, HIGH);
        Serial.print("steps:");
        delay(warten);
      }

      if(String(inData)=="QQQ"){
        digitalWrite(MotorE_R, LOW);
        digitalWrite(MotorE_L, HIGH);
        Serial.print("steps:");
        delay(warten);
      }

      if(String(inData)=="QQQQ"){
        digitalWrite(MotorE_R, LOW);
        digitalWrite(MotorE_L, HIGH);
        Serial.print("steps:");
        delay(warten);
      }

      //Motr für das D
      if(String(inData)=="D"){
        digitalWrite(MotorD_R, HIGH);
        digitalWrite(MotorD_L, LOW);
        Serial.print("steps:");
        delay(warten);
      }

      if(String(inData)=="D"){
        digitalWrite(MotorD_R, HIGH);
        digitalWrite(MotorD_L, LOW);
        Serial.print("steps:");
        delay(warten);
      }

      if(String(inData)=="DD"){
        digitalWrite(MotorD_R, HIGH);
        digitalWrite(MotorD_L, LOW);
        Serial.print("steps:");
        delay(warten);
      }
      
      if(String(inData)=="DDD"){
        digitalWrite(MotorD_R, HIGH);
        digitalWrite(MotorD_L, LOW);
        Serial.print("steps:");
        delay(warten);
      }

      if(String(inData)=="U"){
        digitalWrite(MotorD_R, LOW);
        digitalWrite(MotorD_L, HIGH);
        Serial.print("steps:");
        delay(warten);
      }

      if(String(inData)=="UU"){
        digitalWrite(MotorD_R, LOW);
        digitalWrite(MotorD_L, HIGH);
        Serial.print("steps:");
        delay(warten);
      }

      if(String(inData)=="UUU"){
        digitalWrite(MotorD_R, LOW);
        digitalWrite(MotorD_L, HIGH);
        Serial.print("steps:");
        delay(warten);
      }

      for ( i = 0; i < remainf_bytes; i++){
        inChar=serial_connection.read();
      }
      
//das hier ist der Notfall Stop der eigentlich nie verwedet werden muss

      // if (String(inData)=="P"){
      //   digitalWrite(MotorA_L, LOW);
      //   digitalWrite(MotorA_R, LOW);
      //   Serial.print("steps:");
      //   Serial.println("counterclockwise");
      //   delay(warten);
      // } 
      Serial.println(inData);
      Serial.println(inData);

// F aus
      digitalWrite(MotorF_R, LOW);
      digitalWrite(MotorF_L, LOW);

// A aus
      digitalWrite(MotorA_L, LOW);
      digitalWrite(MotorA_R, LOW);

// D aus
      digitalWrite(MotorD_L, LOW);
      digitalWrite(MotorD_R, LOW);

// E aus
      digitalWrite(MotorE_L, LOW);
      digitalWrite(MotorE_R, LOW);

// C aus
      digitalWrite(MotorC_L, LOW);
      digitalWrite(MotorC_R, LOW);

// G aus
      digitalWrite(MotorG_L, LOW);
      digitalWrite(MotorG_R, LOW);
    }
        
}