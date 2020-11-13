#include <Arduino.h>
#include <SoftwareSerial.h>

int enablePin = 6;
int RichtungEins = 7;
int ReichtungZwei = 8;
//Servo myservo;

SoftwareSerial serial_connection(2, 3);
#define BUFFER_SIZE 64
const int stepsPerRevolution = 50;
// Stepper Stepper1(stepsPerRevolution, 4, 5, 6, 7);
char inData[BUFFER_SIZE];
char inChar=-1;
int count=0;
int i = 0;
int winkel = 90;
int warten = 10;
int UmWievielSichDerServoDrehenSOll = 200;
int first_bytes;
int remainf_bytes=0;
byte byte_count;
int stepCount = 0; 
int steps = 3;

void setup() {
  // Stepper1.setSpeed(60);
  Serial.begin(9600);//9600);
  serial_connection.begin(9600);//9600);
  serial_connection.println("Ready!!");
  Serial.println("Started");

  //myservo.attach(9);

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
      
      if (String(inData)=="N"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }

         if (String(inData)=="FN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }

         if (String(inData)=="NFN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }

        if (String(inData)=="NNNNNN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }
      if (String(inData)=="FFNNNNNNNNNFFNNN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }
      if (String(inData)=="FNNNNNNNFFNNNNNNNNN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }
      if (String(inData)=="FNFNNNNNNNFFFFNNNNNNN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }
      if (String(inData)=="FFNNNNNNNNN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }


      if (String(inData)=="FFFFNNNNNNNFFFFNNNNNNN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }
      if (String(inData)=="FFFFNNNNNNN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }

      if (String(inData)=="FFNNNNNNNNN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }
       if (String(inData)=="FNNNNNNNNNFFNNNNNNNNN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }
       if (String(inData)=="NFFNNNNNNNNN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }
       if (String(inData)=="FFNNNNNNNN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }
      
       if (String(inData)=="FFNNNNNNNNNFFNNNNNNNNN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }
      
       if (String(inData)=="NNNNNNFFNNNNNNNNN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }

      if (String(inData)=="FN"){
        Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
        Serial.print("steps:");
        Serial.println("clockwise");
        delay(warten);
      } else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }
      if (String(inData)=="FNFFN"){
       Serial.println(inData);
      digitalWrite(RichtungEins, HIGH);
        digitalWrite(ReichtungZwei, LOW);
       Serial.print("steps:");
       Serial.println("clockwise");
       delay(warten);
      } else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }


      if (String(inData)=="F"){
        Serial.println(inData);
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      } else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }
      
if (String(inData)=="FF"){
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");

        delay(warten);
      } else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }

if (String(inData)=="FFFFF"){
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      }
 else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }
      if (String(inData)=="FFFFFFFFF"){
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, HIGH);
        Serial.print("steps:");
        Serial.println("counterclockwise");
        delay(warten);
      }
      else {
        digitalWrite(RichtungEins, LOW);
        digitalWrite(ReichtungZwei, LOW);
      }
      for ( i = 0; i < remainf_bytes; i++){
        inChar=serial_connection.read();
      }
      
      Serial.println(inData);
      Serial.println(inData);
    }
        
}