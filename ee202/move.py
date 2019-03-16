import serial
import pyautogui
import numpy as np
ser = serial.Serial('/dev/tty.usbmodem1412', 9600, bytesize=8, timeout=2)
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.01

MOVE_FACTOR = 0.4

coffe_1 = [ 5.58675920e-03, -2.97219778e-04, -6.81021883e-05, -3.12608831e-04]
bias_1 = -1.1

in_process = 0
t = 0
gx_buffer = [0,0,0]

while(ser.is_open):
    line = ser.readline()
    d_line = str(line,encoding='utf-8',errors='strict')
    cop = str(d_line)
                #print(d_line)
    s = cop.split(" ")
                #print(s)
    gx = float(s[0])
    gy = float(s[1])
    gz = float(s[2])
    roll = float(s[3])
    pitch = float(s[4])
    ax = float(s[5])
    ay = float(s[6])
    az = float(s[7])

    if t<3 :
        gx_buffer[t] = gx
        t = t + 1
    else :
        gx_buffer[0] = gx
        t = 1

    vx = roll
    vy = pitch
    if(in_process == 0):
        if np.dot([gx,gz,roll,pitch],coffe_1) + bias_1 > 0 :
            pyautogui.scroll(-5)
        #print(s)
        elif(abs(vx) > 10 or abs(vy) > 10):
            if vx > 10:
                vx = vx - 10
            elif vx < -10:
                vx = vx + 10
            if vy > 10 :
                vy = vy - 10
            elif vy < -10:
                vy = vy + 10
            pyautogui.moveRel(vx*MOVE_FACTOR,-vy*MOVE_FACTOR)
            pyautogui.moveRel(vx*MOVE_FACTOR,-vy*MOVE_FACTOR)
            pyautogui.moveRel(vx*MOVE_FACTOR,-vy*MOVE_FACTOR)
            pyautogui.moveRel(vx*MOVE_FACTOR,-vy*MOVE_FACTOR)
            pyautogui.moveRel(vx*MOVE_FACTOR,-vy*MOVE_FACTOR)
        if (in_process == 1):
            if gx_buffer[0] < 5 and gx_buffer[1] < 5 and gx_buffer[2] < 5:
                in_process = 0

ser.close()
