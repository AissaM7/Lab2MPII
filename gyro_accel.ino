#include <MPU6050_light.h>
#include <Wire.h>

const int MPU = 0x68; // I2C address of the MPU-6050. .
int16_t gx, gy; // variables for gyro

char tmp[7]; // temporary variable used in convert function

char* convert_int16_to_str(int16_t i) { // converts int16 to string. Moreover, resulting strings will have the same length in the debug monitor.
  sprintf(tmp, "%6d", i);
  return tmp;
}

void setup() {
  //code to read data from python for beep
 if(Serial.available() > 0){
    serialData =  Serial.readStringUntil('\n');
      if(serialData == '1'){
        digitalWrite(pin, HIGH);
        delay(1000);
        digitalWrite(pin, LOW);
      }
  }
  Serial.begin(9600);
  Wire.begin();
  Wire.beginTransmission(MPU); // starts a transmission to the I2C slave (GY-521 board)
  Wire.write(0x6B); // PWR_MGMT_1 register
  Wire.write(0); // wakes up the MPU-6050
  Wire.endTransmission(true);
}
void loop() {
  Wire.beginTransmission(MPU);
  Wire.write(0x3B); // starting with register 0x3B 
  Wire.endTransmission(false); // the parameter indicates that the Arduino will send a restart, the connection is kept active.
  Wire.requestFrom(MPU, 7*2, true); // request total of 7*2=14 registers
  
  // "Wire.read()<<8 | Wire.read();" means two registers are read and stored in the same variable
  gx = Wire.read()<<8 | Wire.read(); // reading registers: 0x43 (GYRO_XOUT_H) and 0x44 (GYRO_XOUT_L)
  gy = Wire.read()<<8 | Wire.read(); // reading registers: 0x45 (GYRO_YOUT_H) and 0x46 (GYRO_YOUT_L)
  
  // print out data
  // the following equation was taken from the documentation [MPU-6000/MPU-6050 Register Map and Description, p.30]
 
  Serial.print("X"); Serial.print(convert_int16_to_str(gx));
  Serial.print("Y"); Serial.print(convert_int16_to_str(gy));
  Serial.println();
  
  // delay
  delay(1000);
}
