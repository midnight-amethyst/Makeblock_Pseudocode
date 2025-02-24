from robot import *

motor1 = Motor('motor1')
motor2 = Motor('motor2')
motorGrabber = Motor('Grabber')
motorArm = Motor('Arm')
sensor = Sensor()


counter = 0



def move(N):
    motor1.run(100)
    motor2.run(100)
    delay(N)
    
    pass

def turn(Right):
    if Right == True;
        motor1.run(-100)
        motor2.run(100)
        delay(1000)
        motor1.stop
        motor2.stop
    elif Right == False;
        motor1.run(100)
        motor2.run(-100)
        delay(1000)
        motor1.stop
        motor2.stop
    
    pass

def sensing()
    while distance >100 and len(distance_data)==0:
        turn(False)
    else:
        distance_data.append(distance)
        distance_data_sort = distance_data.sort()
        if distance_data[-1] == distance_data_sort(0):
            turn(False)
        else:
            turn()
            
       
    

def grab():
    # Grab
    # Arm up
    return True

def release():
    pass


while True:


    counter += 1

    # Move forwards until distance is close enoguh
    # Grab (switch modes)
    # Find the box by rotating
    # Move forwards towards box
    # Release

    distance = sensor.measure_distance()
    distance_data=[]

    # Move initial
    if distance >= 10 and counter < 30:
        move()
    elif distance < 10 and counter < 30:
        motor1.stop()
        motor2.stop()
        grab()
    elif counter >= 30 and counter < 40:
        turn()
        # Provide data
    elif counter >= 40 and counter < 50 and distance + 1> "provided distance":
        turn()
    elif distance <= "provided distance" + 1:
        motor1.stop()
        motor2.stop()
    elif counter >= 50 and distance >= 10:
        move()
    elif counter >= 50 and distance < 10:
        motor1.stop()
        motor2.stop()
        release()



