int verticalRead = A0;
int horizontalRead = A1;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
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
joystickinputs.ino
