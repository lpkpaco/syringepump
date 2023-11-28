import RPi.GPIO as GPIO
import time
import multiprocessing as multi
import fx.forward as forward
import fx.reverse as reverse
print("CPU cores available: " + multi.cpu_count())
pool = multi.Pool()
forward = multi.Process(target=forward())
reverse = multi.Process(target=reverse())
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
            reverse()
            counting += 1
        if x > 0:
            forward()
            counting += 1
    GPIO.cleanup()
    exit()