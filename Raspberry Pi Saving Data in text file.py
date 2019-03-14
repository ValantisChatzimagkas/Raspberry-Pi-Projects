# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from Adafruit_BME280 import *
import datetime

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8)#saves samples like : sensor = (temperature,pressure)
temperature = sensor.read_temperature()#we access the temperature read of the sensor variable
pressure = (sensor.read_pressure())/100#we access the pressure read of the sensor variable and we format it in hectopascals with /100

timestamp = datetime.datetime.now().replace(microsecond=0)#we save the current date and time 
                                                          #the .replace(microsecond=0) removes microseconds which are being read

file = open('text_datalog.txt','a')# we open the file which we have saved in the same location as our code,
                                  #the 'a' parameter appends data at the end of file, does not truncate and creates file if it doesn't exist
file.write("Sample taken at {} ".format(timestamp))#we write current data and time in file
file.write("Temperature = {:.4f} ".format(temperature ))#we write temperature sample with 4 digit accuracy
file.write("Pressure = {:.4f} ".format(pressure))#we write pressure sample with 4 digits accuracy
file.write("\n")#we change to avoid writting all data is the same line
file.close()#we close the file ass soon as we finish



""" PART 2 IMPLEMENTATION WITH THE USE OF A FUNCTION  """
from Adafruit_BME280 import *
import datetime
import time

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8)
temperature = sensor.read_temperature()
pressure = (sensor.read_pressure())/100

timestamp = datetime.datetime.now().replace(microsecond=0)


def datalogging(option):


    if option == 'sample':
            print('operating in fixed amount of samples mode')
            samples = int(input('Enter number of samples '))

            for i in range(samples):
                file = open('text_datalog.txt','a')
                file.write("Sample taken at {} ".format(timestamp))
                file.write("Temperature = {:.4f} ".format(temperature ))
                file.write("Pressure = {:.4f} ".format(pressure))
                file.write("\n")
                time.sleep(1)
    elif option == 'loop':
        try:
            while True:
                print('operating in endless loop mode')
                file = open('text_datalog.txt', 'a')
                file.write("Sample taken at {} ".format(timestamp))
                file.write("Temperature = {:.4f} ".format(temperature))
                file.write("Pressure = {:.4f} ".format(pressure))
                file.write("\n")
                time.sleep(1)
        except KeyboardInterrupt:
            pass
    else:
        print('not a valid option')


print('Executing txt datalogging code')
option = str(input('Type sample to set fixed amount of samples or loop for endless looping : '))

datalogging(option)



