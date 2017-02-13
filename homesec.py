import thread
import serial
import time

# Default state is no motion.
global zone2
global zone3
global zone4
global zone5
global zone6
# Clunky hard-coded device
ser = serial.Serial('/dev/ttyUSB0')

# Fix this eventually...
#def open_serial():
#        print "Connecting..."
#        ser = serial.Serial('/dev/ttyUSB0')  # open serial port
#        return

def close_serial():
    print "Disconnecting..."
    ser.close()
    return

# Polls the serial connection until it finds  
# status for the specified pin. This is 
# a dangerious game to be playing though.
# There should be a timeout with consequences.
# If an invalid pin is requested or the 
# controller never reports it, this will never
# return.
#TODO: Add timeout
#TODO:  Add awareness of stale data
#TODO: Eventually find a less clunky method for
#      having the controller report status. 
#      Querying for state is ideal, but getting
#      the controller to talk serial both ways 
#      can be a pain.
# Pins:
#   2: Basement
#
def get_sensor_state( pin ):
    pin_match = "PIN: " + str(pin)
    while True:
        line = ser.readline()
        if pin_match in line:
            if "MOTION" in line:
                print "ZONE " + str(pin)
                return True
            if "STILL" in line:
                return False
    return

def sensor_loop():
    while ser.is_open:
        zone2 = get_sensor_state( 2 )
        zone3 = get_sensor_state( 3 )
        zone4 = get_sensor_state( 4 )
        zone5 = get_sensor_state( 5 )
        zone6 = get_sensor_state( 6 )
    return

def main():
    zone2 = zone3 = zone4 = zone5 = zone6 = False
    thread.start_new_thread ( sensor_loop, () )
    while 1:
        time.sleep(1)
    close_serial()
    return

main()
