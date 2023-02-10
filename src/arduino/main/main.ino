int ir = 2; // This is our input pin for IR Sensor
void setup()
{
  pinMode(ir, INPUT);
  Serial.begin(9600);
}
void loop()
{
  int full = digitalRead(ir);
  if (full = HIGH)
  {
    Serial.print("Obstacle Detected! ");
  }
  else
  {
    Serial.print("Path is clear! ");
  }
  Serial.println(full);
  delay(500);
}