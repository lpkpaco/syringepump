try:
    import RPi.GPIO as GPIO
    import time
except:
    pass
def forward(out1, out2, out3, out4, timex, x):
    for y in range(x,0,-1):
        global negative
        global i
        if negative==1:
            if i==7:
                i=0
            else:
                i=i+1
            y=y+2
            negative=0
        positive=1
        #print((x+1)-y)
        if i==0:
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(timex)
            #time.sleep(1)
        elif i==1:
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(timex)
            #time.sleep(1)
        elif i==2:  
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(timex)
            #time.sleep(1)
        elif i==3:    
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.HIGH)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(timex)
            #time.sleep(1)
        elif i==4:  
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.LOW)
            time.sleep(timex)
            #time.sleep(1)
        elif i==5:
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.HIGH)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(timex)
            #time.sleep(1)
        elif i==6:    
            GPIO.output(out1,GPIO.LOW)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(timex)
            #time.sleep(1)
        elif i==7:    
            GPIO.output(out1,GPIO.HIGH)
            GPIO.output(out2,GPIO.LOW)
            GPIO.output(out3,GPIO.LOW)
            GPIO.output(out4,GPIO.HIGH)
            time.sleep(timex)
            #time.sleep(1)
        if i==7:
            i=0
            continue
        i=i+1