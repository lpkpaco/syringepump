import RPi.GPIO as GPIO
import time
GPIO.cleanup()
global negative
global positive
out1 = 17
out2 = 18
out3 = 27
out4 = 23
#defie time variable
timex=0.005
positive=0
negative=0
y=0
overflow = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(out1,GPIO.OUT)
GPIO.setup(out2,GPIO.OUT)
GPIO.setup(out3,GPIO.OUT)
GPIO.setup(out4,GPIO.OUT)
x = 0
global i
i = 0
def forward():
    if overflow == 0:
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
    elif overflow == 1:
        return
    else:
        print("Error")
        exit()
def reverse():
    if overflow == 0:
        global x
        global positive
        global i
        x=x*-1
        for y in range(x,0,-1):
            if positive==1:
                if i==0:
                    i=7
                else:
                    i=i-1
                y=y+3
                positive=0
            negative=1
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
            if i==0:
                i=7
                continue
            i=i-1
    elif overflow == 1:
        return
    else:
        print("Error")
        exit()
def demo():
    global count
    global x
    count = 0 
    while count <= 2:
        if x < 0:
            x = -(x)
        forward()
        if x > 0:
            x = -(x)
        reverse()
        reverse()                                                                                                                                                                           
        count += 1
try:
   while(1):
      GPIO.output(out1,GPIO.LOW)
      GPIO.output(out2,GPIO.LOW)
      GPIO.output(out3,GPIO.LOW)
      GPIO.output(out4,GPIO.LOW)
      x = input()
      global stepcount
      stepcount = 0
      try:
        x= int(x)
      except:
          continue
      if x>0 and x<=400:
        x = 1
        while True:
            forward()
            stepcount += 1
            print(stepcount)
      elif x<0 and x>=-400:
        x = -1
        while True:
            reverse()
            stepcount += 1
            print(stepcount)
except KeyboardInterrupt:
    overflow = 1
    print(stepcount)
    time.sleep(0.5)
    x = -(x)
    global counting
    counting = 0
    while counting <= stepcount:
        if x < 0:
            overflow = 0
            reverse()
            counting += 1
            continue
        if x > 0:
            overflow = 0
            forward()
            counting += 1
            continue
        overflow = 1
    overflow = 1
    GPIO.cleanup()
    exit()
