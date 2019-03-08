from datetime import datetime
from ds18b20 import read_temp
from thingspeak import post_thingspeak
from display import show_lines
from dotenv import load_dotenv
load_dotenv()

temp_c = read_temp()
print('C=%3.3f' % temp_c)

# send to IOT platform
post_thingspeak(temp_c)

# display on local LCD in this format:
# Line 1: Now: 17:25:40
# Line 2: T1 = 23.7 C
display_data = []
display_data.append(datetime.now().strftime('Now: %H:%M:%S'))
temp_c = str(round(temp_c * 10) / 10)
display_data.append('T1 = ' + temp_c + ' C')
show_lines(display_data)
