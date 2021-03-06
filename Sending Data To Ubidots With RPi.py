# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import requests
from Adafruit_BME280 import *
import time
sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8)
TOKEN = "YOUR TOKEN"  # Put your TOKEN here
DEVICE_LABEL = "raspberry3"  # Put your device label here
VARIABLE_LABEL_1 = "temperature"  # Put your first variable label here
VARIABLE_LABEL_2 = "pressure"  # Put your second variable label here

def build_payload(variable_1, variable_2):
    value_1 = sensor.read_temperature()#Temperature
    value_2 = sensor.read_pressure()#Pressure

    payload = {variable_1: value_1,
               variable_2: value_2}
    return payload
	
def post_request(payload):
    #Ths function creates headers for the HTTP requests
    url = "http://things.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
    # Construction of HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
		time.sleep(1)
    # Checks results
    if status >= 400:
        print("ERROR!!! Could not send data after 5 attempts, please check \
            if your token credentials are wrong or if your internet connection is down ")
        return False
    print("SUCCESS!!! request has been succesful, your data has been updated")
    return True

def main():
    payload = build_payload(
        VARIABLE_LABEL_1, VARIABLE_LABEL_2)
    print("Attempting to send data...")
    post_request(payload)
    print("Process finished")
    print("Request has been succesful, your data has been updated")
    return True
if __name__ == '__main__':
    while (True):
        main()
        time.sleep(1)
