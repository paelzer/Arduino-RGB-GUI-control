int incomingByte = 0; // for incoming serial data
String myString;

int bluePin  = 11;
int greenPin = 10;
int redPin   = 9;
long myStringInt = 0;

void setup() {

  pinMode(redPin,   OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin,  OUTPUT);

  Serial.begin(9600);
  Serial.setTimeout(10);  // improves the serial response time
}

void loop() {

  myString = getSerial();

  if (myString.startsWith("#"))    { // "#" determines value is RGB
    myString.remove(0, 1);          // removes "#" to only have the numbers
    myStringInt = myString.toInt(); // converts myString from a string to an integer
    setSelectedRGB(myStringInt);    // send the integer value to the function which activates the RGB pins
  }
}

String getSerial()  {
  String a;
  while (Serial.available())   {
    //if (a != "\n")    {
    a = Serial.readString();
    //}
  }

  return (a);
}


void setSelectedRGB(long colorValue)   {
  //Serial.println(colorValue);
  analogWrite(redPin, (colorValue >> 16));
  //Serial.println(colorValue >> 16);
  analogWrite(greenPin, ((colorValue & 0xFF00) >> 8));
  //Serial.println((colorValue & 0xFF00) >> 8);
  analogWrite(bluePin, (colorValue & 0xFF));
  //Serial.println(colorValue & 0xFF);
}
