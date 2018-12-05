
import curses
import RPi.GPIO as GPIO

#=============================================================================
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
p1 = GPIO.PWM(12, 100)
p2 = GPIO.PWM(32, 100)
p1.start(0)
p2.start(0)
p1.ChangeDutyCycle(30)
p2.ChangeDutyCycle(30)#droite
# ============================================================================

screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)
def forward():
    GPIO.output(31,True)
    GPIO.output(33,False)
    GPIO.output(35,False)
    GPIO.output(37,True)
def turn_left():
    GPIO.output(31,False)
    GPIO.output(33,True)
    GPIO.output(35,False)
    GPIO.output(37,True)
def turn_right():
    GPIO.output(31,True)
    GPIO.output(33,False)
    GPIO.output(35,True)
    GPIO.output(37,False)
def stop():
    GPIO.output(31,False)
    GPIO.output(33,False)
    GPIO.output(35,False)
    GPIO.output(37,False)
def back():
    GPIO.output(31,False)
    GPIO.output(33,True)
    GPIO.output(35,True)
    GPIO.output(37,False)
try:
        print("============================================================")
        print("====================commande vocale du robot================")
        print("============================================================")
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                    forward()

            elif char == curses.KEY_DOWN:
                    
                    back()
                    
            elif char == curses.KEY_RIGHT:
                    turn_right()
            elif char == curses.KEY_LEFT:
                    turn_left()
            elif char == 10:
                    stop()
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    
