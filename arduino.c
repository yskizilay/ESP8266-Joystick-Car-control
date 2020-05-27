
#include <ArduinoJson.h>

bool debugmode = false;
const int Enable_A = 2;
const int Enable_B = 3;
const int Enable_C = 4;
const int Enable_D = 5;
const int inputA1 = 22;
const int inputA2 = 23;
const int inputB1 = 24;
const int inputB2 = 25;
const int inputC1 = 26;
const int inputC2 = 27;
const int inputD1 = 28;
const int inputD2 = 29;

void setup() {
Serial1.begin(115200);
Serial.begin(115200);
pinMode(Enable_A, OUTPUT);
pinMode(Enable_B, OUTPUT);
pinMode(Enable_C, OUTPUT);
pinMode(Enable_D, OUTPUT);
pinMode(inputA1, OUTPUT);
pinMode(inputA2, OUTPUT);
pinMode(inputB1, OUTPUT);
pinMode(inputB2, OUTPUT);
pinMode(inputC1, OUTPUT);
pinMode(inputC2, OUTPUT);
pinMode(inputD1, OUTPUT);
pinMode(inputD2, OUTPUT);
digitalWrite(Enable_A, LOW);
digitalWrite(Enable_B, LOW);
digitalWrite(Enable_C, LOW);
digitalWrite(Enable_D, LOW);
digitalWrite(inputA1, LOW);
digitalWrite(inputA2, LOW);
digitalWrite(inputB1 , LOW);
digitalWrite(inputB2, LOW);
digitalWrite(inputC1, LOW);
digitalWrite(inputC2, LOW);
digitalWrite(inputD1 , LOW);
digitalWrite(inputD2, LOW);
}


void loop() {
    while (Serial1.available() > 0){
       String my_name = Serial1.readStringUntil('\n');
        StaticJsonDocument<1024> doc;
        DeserializationError error = deserializeJson(doc, my_name);

  // Test if parsing succeeds.
  if (error) {
    if (debugmode){
      Serial.print(F("deserializeJson() failed: "));
      Serial.println(error.c_str());
      }
    return;
  } 
    String joystickName = doc["joystickdata"]["joystickName"];
    String localtime = doc["localtime"];
    int axisx = doc["joystickdata"]["axisx"];
    int axisy = doc["joystickdata"]["axisy"];
    int axisz = doc["joystickdata"]["axisz"];
    int axist = doc["joystickdata"]["axist"];
    bool valbutton0 = doc["joystickdata"]["valbutton0"];
    bool valbutton1 = doc["joystickdata"]["valbutton1"];
    bool valbutton2 = doc["joystickdata"]["valbutton2"];
    bool valbutton3 = doc["joystickdata"]["valbutton3"];
    bool valbutton4 = doc["joystickdata"]["valbutton4"];
    bool valbutton5 = doc["joystickdata"]["valbutton5"];
    bool valbutton6 = doc["joystickdata"]["valbutton6"];
    bool valbutton7 = doc["joystickdata"]["valbutton7"];
    bool valbutton8 = doc["joystickdata"]["valbutton8"];
    bool valbutton9 = doc["joystickdata"]["valbutton9"];
    bool valbutton10 = doc["joystickdata"]["valbutton10"];
    bool valbutton11 = doc["joystickdata"]["valbutton11"];
    bool valhatbutton0 = doc["joystickdata"]["valhatbutton0"];
    bool valhatbutton1 = doc["joystickdata"]["valhatbutton1"];
    bool valhatbutton2 = doc["joystickdata"]["valhatbutton2"];
    bool valhatbutton3 = doc["joystickdata"]["valhatbutton3"];

  
    motorforward( axisx, axisy, axisz, axist);
    
    //Serial.println(" x: " + String(axisx) + " y: " + String(axisy) + " z: " + String(axisz) + " t: " + String(axist) );

    }
}

void motorforward(int axisx, int axisy, int axisz, int axist){
  if (axist > '0'){
      analogWrite(Enable_A, axist);
      analogWrite(Enable_B, axist);
      analogWrite(Enable_C, axist);
      analogWrite(Enable_D, axist);
      digitalWrite(inputA1, HIGH);
      digitalWrite(inputA2, LOW);
      digitalWrite(inputB1 , HIGH);
      digitalWrite(inputB2, LOW);
      digitalWrite(inputC1, HIGH);
      digitalWrite(inputC2, LOW);
      digitalWrite(inputD1 , HIGH);
      digitalWrite(inputD2, LOW);
     
    }
   if (axist < '0'){
      analogWrite(Enable_A, abs(axist));
      analogWrite(Enable_B, abs(axist));
      analogWrite(Enable_C, abs(axist));
      analogWrite(Enable_D, abs(axist));
      digitalWrite(inputA1, LOW);
      digitalWrite(inputA2, HIGH);
      digitalWrite(inputB1 , LOW);
      digitalWrite(inputB2, HIGH);
      digitalWrite(inputC1, LOW);
      digitalWrite(inputC2, HIGH);
      digitalWrite(inputD1 , LOW);
      digitalWrite(inputD2, HIGH);

    }

     if (axist == '0'){
      analogWrite(Enable_A, 0);
      analogWrite(Enable_B, 0);
      analogWrite(Enable_C, 0);
      analogWrite(Enable_D, 0);
      digitalWrite(inputA1, LOW);
      digitalWrite(inputA2, LOW);
      digitalWrite(inputB1 , LOW);
      digitalWrite(inputB2, LOW);
      digitalWrite(inputC1, LOW);
      digitalWrite(inputC2, LOW);
      digitalWrite(inputD1 , LOW);
      digitalWrite(inputD2, LOW);

    }


  }
          

       
