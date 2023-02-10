int obstaclePin = A1; // This is our input pin
void setup()
{
  pinMode(obstaclePin, INPUT);
  Serial.begin(9600);
}
void loop()
{
  int hasObstacle = analogRead(obstaclePin);
  // Serial.println(hasObstacle);
  if (hasObstacle < 50)
  {
    Serial.print("Obstacle Detected! ");
  }
  else
  {
    Serial.print("Path is clear! ");
  }
  Serial.println(hasObstacle);
  delay(500);
  /*
  if (hasObstacle > )

  {
    Serial.print( "Stop something is ahead!!  ");
    Serial.println(hasObstacle);
  }
  else
  {
    Serial.print("Path is clear  ");
    Serial.println(hasObstacle);
  }
  */
  // delay(100);
}