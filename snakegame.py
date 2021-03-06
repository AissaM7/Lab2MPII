# Simple Snake Game in Python 3 for Beginners
# By @TokyoEdTech
# modified by Yan Luo
# modified by Russell Soto, Deven Burrowes, Aissa Mamdouh


import turtle
import time
import random
import serial
# TODO uncomment the following line to use pyserial package
#import serial

t = 0
# Note the serial port dev file name
# need to change based on the particular host machine
# TODO uncomment the following two lines to initialize serial port
#serialDevFile = '/dev/cu.usbmodem14201'
#ser=serial.Serial(serialDevFile, 9600, timeout=0)

delay = 0.1

# Score
score = 0
high_score = 0
ppa = 10

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @TokyoEdTech (mod by YL)")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0  P/A: 10", align="center", font=("Courier", 24, "normal"))

#functions
def Buzzer_on():
    yourSerial = serial.Serial('COM4')
    yourSerial.timeout = 1
    yourSerial.write(str.encode('1'))
    yourSerial.close()
def move():
    #if statements used to check where to move snake if joystick or gyro has been moved
    
    if (vertical > 0 and horizontal == 0 or vertical > 8000): 
        y = head.ycor()
        head.sety(y + 20)

    if (vertical < 0 and horizontal == 0 or vertical < -8000):
        y = head.ycor()
        head.sety(y - 20)

    if (horizontal > 0 and vertical == 0 or horizontal > 8000):
        x = head.xcor()
        head.setx(x - 20)

    if (horizontal < 0 and vertical == 0 or horizontal < -8000):
        x = head.xcor()
        head.setx(x + 20)
    

# Keyboard bindings
#wn.listen()
# Main game loop
while True:
    wn.update()
    #serial for usb being set to variable
    yourSerial= serial.Serial('COM4')
    #data read from usb being put into string
    joystickData = str(yourSerial.readline())
    #setting variable for vertical movement as it being read from arduino 
    vertical = int(joystickData[3:joystickData.find('Y')])
    #setting variable for horizontal movement as it being read from arduino
    horizontal = int(joystickData[joystickData.find('Y') + 1: joystickData.find('\\')])
    #printing the data
    print(vertical,horizontal)
    #closing the connection from the usb when one cycle of while loop has been completed
    yourSerial.close()
    

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}  P/A: {}".format(score, high_score, ppa), align="center", font=("Courier", 24, "normal")) 


    # Check for a collision with the food
    if head.distance(food) < 20:
        Buzzer_on()
       
     

        # TODO: notes by Prof. Luo
        # you need to send a flag to Arduino indicating an apple is eaten
        # so that the Arduino will beep the buzzer
        # Hint: refer to the example at Serial-RW/pyserial-test.py

        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}  P/A: {}".format(score, high_score, ppa), align="center", font=("Courier", 24, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}  P/A: {}".format(score, high_score, ppa), align="center", font=("Courier", 24, "normal")) 

    time.sleep(delay)

wn.mainloop()
