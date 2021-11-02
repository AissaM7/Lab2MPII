int verticalRead = A0;
int horizontalRead = A1;
String serialData;
int pin = 7;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(pin,OUTPUT);
  
}

void loop() {
  //code to read data from python for beep
  if(Serial.available() > 0){
    serialData =  Serial.readStringUntil('\n');
      if(serialData == '1'){
        digitalWrite(pin, HIGH);
        delay(1000);
        digitalWrite(pin, LOW);
      }
      }
  // put your main code here, to run repeatedly:
  String vertical = String(map((analogRead(verticalRead)- 4), 0, 1023, -5, +6));
  String horizontal = String(map((analogRead(horizontalRead) + 4), 0, 1023, -5, +5));

  if (vertical != "0" || horizontal != "0") {
    String toReturn = "X";
    toReturn += vertical;
    toReturn += "Y";
    toReturn += horizontal;
    toReturn += 
    Serial.println(toReturn);
    delay(40);
  }
}
