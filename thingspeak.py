import os
import urllib.request
import urllib.parse
from dotenv import load_dotenv
load_dotenv()


def post_thingspeak(temp1):
    values = {'api_key' : os.environ['THINGSPEAKKEY'], 'field1' : temp1}
    querystring = urllib.parse.urlencode(values)
    postdata = querystring.encode('ascii')
    response = urllib.request.urlopen(os.environ['THINGSPEAKURL'], postdata)
    response.read()
    response.close()
