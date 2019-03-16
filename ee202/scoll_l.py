from pynput import mouse
from pynput.mouse import Button, Controller
import logging
import os
import serial


ser = serial.Serial('/dev/tty.usbmodem1442', 9600, bytesize=8, timeout=2)

cwd = os.getcwd()
log_directory = os.path.join(cwd,"Key_logs")
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

i = 1
while os.path.exists("scroll_log%s.txt" %i):
    i += 1

#log_dir = ""
#logging.basicConfig(filename = (log_dir + "key_log%s.txt" % i), level=logging.INFO, format='%(asctime)s.%(msecs)03d,%(message)s', datefmt='%s')

formatter = logging.Formatter('%(asctime)s.%(msecs)03d,%(message)s', datefmt='%s')
def setup_logger(name, log_file, level=logging.INFO):
    """Function setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

#mouse_logger = setup_logger('mouse_logger', 'mouse_log%s.txt' %i)
scoll_logger = setup_logger('scoll_logger','scoll_log%s.txt'%i)
while(ser.is_open):
    line = ser.readline()
    d_line = str(line,encoding='utf-8',errors='strict')
    cop = str(d_line)
    s = cop.split(" ")
    scoll_logger.info(' %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f %4.2f',\
                    float(s[0]),float(s[1]),float(s[2]),float(s[3]),\
                     float(s[4]),float(s[5]),float(s[6]),float(s[7]))
