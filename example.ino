void setup()
{
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  Serial.begin(9600);
}

void loop()
{
  if(Serial.read() == '0')
  {
    digitalWrite(13, LOW);
    
  }

  if(Serial.available()>0)
  {
    digitalWrite(13, HIGH);
  }
}
