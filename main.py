import RPi.GPIO as GPIO
import time
import multiprocessing as multi
from multiprocessing import Process
import fx.forward as forward
import fx.reverse as reverse
import os
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
if __name__ == "__main__":
    pf = Process(target=forward.forward, args=(out1, out2, out3, out4, timex, x,))
    pr = Process(target=reverse.reverse, args=(out1, out2, out3, out4, timex, x,))
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
                    pf.start()
                    pf.join()
                    stepcount += 1
                    print(stepcount)
                    time.sleep(0.1)
            elif x<0 and x>=-400:
                x = -1
                while True:
                    pr.start()
                    pr.join()
                    stepcount += 1
                    print(stepcount)
                    time.sleep(0.1)
    except KeyboardInterrupt:
        try:
            pf.kill()
            pr.kill()
        except:
            pass
        print(stepcount)
        time.sleep(0.5)
        x = -(x)
        global counting
        counting = 0
        if x < 0:
            while counting <= stepcount:
                pr.start()
                pr.join()
                counting += 1
                time.sleep(0.1)
            pr.kill()
            GPIO.cleanup()
            exit()
        if x > 0:
            while counting <= stepcount:
                pf.start()
                pf.join()
                counting += 1
                time.sleep(0.1)
            pf.kill()
            GPIO.cleanup()
        GPIO.cleanup()
        exit()