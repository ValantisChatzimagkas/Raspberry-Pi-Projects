# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import pymysql
import pymysql.cursors
from Adafruit_BME280 import *

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8)#saves samples like : sensor = (temperature,pressure)

temperature = sensor.read_temperature()#we access the temperature read of the sensor variable
pressure = (sensor.read_pressure())/100#we access the pressure read of the sensor variable and we format it in hectopascals with /100


db = pymysql.connect("YOUR_HOST","YOUR_USERNAME","YOUR_PASSWORD","YOUR_DATABASE" )#creates a variable called db and we provide the credentials to logo
cursor = db.cursor()#"A cursor allows you to iterate a set of rows returned by a query and process each row accordingly" taken from http://www.mysqltutorial.org/mysql-cursor/
cursor.execute("INSERT INTO YOUR_TABLE(temperature,pressure)"\ #inserts data to the specific columns
                  "VALUES('%s','%s')" ,(temperature,pressure))#here we provide the sensor data
db.commit()#here we commit the results in our database


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
              db = pymysql.connect("YOUR_HOST","YOUR_USERNAME","YOUR_PASSWORD","YOUR_DATABASE" )#creates a variable called db and we provide the credentials to logo
              cursor = db.cursor()#"A cursor allows you to iterate a set of rows returned by a query and process each row accordingly" taken from http://www.mysqltutorial.org/mysql-cursor/
              cursor.execute("INSERT INTO YOUR_TABLE(temperature,pressure)" #inserts in your table's collumns the data given below
                  "VALUES('%s','%s')" ,(temperature,pressure))#here we provide the sensor data
              db.commit()#here we commit the results in our database
              time.sleep(1)
                
    elif option == 'loop':
        try:
            while True:
                db = pymysql.connect("YOUR_HOST","YOUR_USERNAME","YOUR_PASSWORD","YOUR_DATABASE" )#creates a variable called db and we provide the credentials to logo
                cursor = db.cursor()#"A cursor allows you to iterate a set of rows returned by a query and process each row accordingly" taken from http://www.mysqltutorial.org/mysql-cursor/
                cursor.execute("INSERT INTO YOUR_TABLE(temperature,pressure)" #inserts in your table's collumns the data given below
                  "VALUES('%s','%s')" ,(temperature,pressure))#here we provide the sensor data
                db.commit()#here we commit the results in our database
                time.sleep(1)
        except KeyboardInterrupt:
            pass
    else:
        print('not a valid option')


print('Executing local database insertion code')
option = str(input('Type sample to set fixed amount of samples or loop for endless looping : '))

datalogging(option)
