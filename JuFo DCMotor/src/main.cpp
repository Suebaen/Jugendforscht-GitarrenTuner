#include <Arduino.h>
#include <SoftwareSerial.h>

int enablePin = 4;
int RichtungEins = 5;
int ReichtungZwei = 6;

int pin11 = 7;
int Richtung1 = 8;
int Richtung2 = 9;

SoftwareSerial serial_connection(2, 3);
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
        // Motor 1
      if (String(inData)=="N"){
        Serial.println(inData);
        digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

 if (String(inData)=="NNN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

 if (String(inData)=="NNNN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 
         if (String(inData)=="FN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

         if (String(inData)=="NFN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

        if (String(inData)=="NNNNNN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 
      if (String(inData)=="F"){
        Serial.println(inData);
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 
      
        if (String(inData)=="FF"){
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 
      if (String(inData)=="FFF"){
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 

//     // Motor 2
      if (String(inData)=="A"){
        Serial.println(inData);
        digitalWrite(Richtung1, HIGH);
        digitalWrite(Richtung2, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

 if (String(inData)=="AA"){
        Serial.println(inData);
        digitalWrite(Richtung1, HIGH);
        digitalWrite(Richtung2, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 
         if (String(inData)=="ABA"){
        Serial.println(inData);
        digitalWrite(Richtung1, HIGH);
        digitalWrite(Richtung2, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

       if (String(inData)=="AAA"){
        Serial.println(inData);
        digitalWrite(Richtung1, HIGH);
        digitalWrite(Richtung2, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 


        if (String(inData)=="AAAAAAA"){
        Serial.println(inData);
        digitalWrite(Richtung1, HIGH);
        digitalWrite(Richtung2, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 
      if (String(inData)=="B"){
        Serial.println(inData);
        digitalWrite(Richtung1, LOW);
        digitalWrite(Richtung2, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 
      
        if (String(inData)=="BB"){
        digitalWrite(Richtung1, LOW);
        digitalWrite(Richtung2, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 
      if (String(inData)=="BBB"){
        digitalWrite(Richtung1, LOW);
        digitalWrite(Richtung2, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 
       if (String(inData)=="BBBB"){
        digitalWrite(Richtung1, LOW);
        digitalWrite(Richtung2, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 


      if (String(inData)=="P"){
        digitalWrite(Richtung1, LOW);
        digitalWrite(Richtung2, LOW);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 
// Motor 3
      if (String(inData)=="C"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

 if (String(inData)=="CC"){
        Serial.println(inData);
        digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 
         if (String(inData)=="CCC"){
        Serial.println(inData);
        digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 

        if (String(inData)=="CCCC"){
        Serial.println(inData);
        digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } 
      if (String(inData)=="D"){
        Serial.println(inData);
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 
      
        if (String(inData)=="DD"){
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 
      if (String(inData)=="DDD"){
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 
       if (String(inData)=="DDDD"){
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } 
      for ( i = 0; i < remainf_bytes; i++){
        inChar=serial_connection.read();
      }
      
      Serial.println(inData);
      Serial.println(inData);
      digitalWrite(RichtungEins, LOW);
      digitalWrite(ReichtungZwei, LOW);
      digitalWrite(Richtung1, LOW);
      digitalWrite(Richtung2, LOW);
    }
        
}