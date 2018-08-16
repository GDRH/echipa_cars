import serial 
mbot = serial.Serial( "/dev/serial0", 115200 )
mbot.write("\xff\x55\x07\x00\x02\x05\x00\x00\x00\x00")