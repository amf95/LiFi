//TX code.

void setup()
{
    Serial.begin(9600);
    pinMode(A0,INPUT);                    //connected to LM35 temperature sesnor. 
}

void loop() 
{
    int Temp = analogRead(A0)*100*5/1023; //read Temperature from LM35 sesnor.
    Serial.println(Temp);                 //send it to the TX LED.
    delay(1000);                          //send data every second.
}
