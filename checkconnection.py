import subprocess
import RPi.GPIO as GPIO
from time import sleep

RED = 32
GREEN = 36
BLINKSTATUS = GPIO.LOW
waitGreen = 1
waitRed = 0.2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED, GPIO.OUT, initial=BLINKSTATUS)
GPIO.setup(GREEN, GPIO.OUT, initial=BLINKSTATUS)

host = "www.google.com"

def blink(led):
    global BLINKSTATUS
    print (BLINKSTATUS)
    if (BLINKSTATUS==GPIO.HIGH):
        BLINKSTATUS=GPIO.LOW
    else:
        BLINKSTATUS=GPIO.HIGH
    print (BLINKSTATUS)

    GPIO.output(led, BLINKSTATUS)
    
def shutdown(led):
    GPIO.output(led, GPIO.LOW)
    
try:

    while (True):
        ping = subprocess.call("ping -c 1 www.google.com",
                               shell=True,
                               stdout=open('/dev/null', 'w'),
                               stderr=subprocess.STDOUT
                               )

        
        
        if(ping==0):
            print("BLINK GREEN")
            shutdown(RED)
            blink(GREEN)
            sleep(waitGreen)
        else:
            print("BLINK RED")
            shutdown(GREEN)
            blink(RED)
            sleep(waitRed)
            
finally:
    GPIO.cleanup()
