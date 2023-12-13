import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)


IN1 = 18
IN2 = 17
IN3 = 27
IN4 = 23

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]

# Function to move the stepper motor
def move_stepper(delay, steps):
    for _ in range(steps):
        for step in sequence:
            GPIO.output(IN1, step[0])
            GPIO.output(IN2, step[1])
            GPIO.output(IN3, step[2])
            GPIO.output(IN4, step[3])
            time.sleep(delay)

# Example usage
try:
    # Set the delay between steps (controls the motor speed)
    delay = 0.001

    # Set the number of steps for rotation
    steps = 512  # Modify this value based on your requirements

    # Rotate the stepper motor clockwise
    move_stepper(delay, steps)

    # Pause for a few seconds
    time.sleep(2)

    # Rotate the stepper motor counterclockwise
    move_stepper(delay, -steps)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
