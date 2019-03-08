from ds18b20 import read_temp
from thingspeak import post_thingspeak
from dotenv import load_dotenv
load_dotenv()

temp_c = read_temp()
print(' C=%3.3f'% temp_c)
post_thingspeak(temp_c)