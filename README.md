# raspi-checkinternet

This is a just for fun project. My ISP is so shitty that I often find myself talking on a conference call and nobody listening me since the connection is down.

I created a simple red/green light dashboard indicating if internet works or not.

NOTE: Of course that if PINGING google doesn't work for any other reason than a connection problem I will have a false negative. Remember, this is J4F!!!

The code is assuming the RED (positive leg) led is binded into pin 32, while green is at 36 (considering GPIO standard, mapped to 12 and 16 on my board at least).

Do you know how to connect a led? You have to put the long leg to currency and the short leg to ground. At some point of the circuit (before or after any the legs) place the proper resistor. If you want to control the led (on and off) the currency should be an output pin.

Get some fun!!!

