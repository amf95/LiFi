//RX code.

void setup() 
{
    Serial.begin(9600);
}



void loop() 
{
      
    if(Serial.available())
    {
      String msg="";

      while(Serial.available())    //read data coming from the RX module. 
      {   
        msg+=(char)Serial.read();    
      }

      Serial.print(msg);           //Send data via serial port to the computer.
    }

    //delay(10);
}
