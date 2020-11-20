import mysql.connector
from decouple import config   # جدید 

mydb = mysql.connector.connect(
  host = config('DB_HOST'), 
  user = config('DB_USER'),
  password = config('DB_PASSWORD'), 
)


RESTART = config('DEBUG', cast=bool)   # برای دریافت اجباری بولین 
EMAIL_PORT = config('EMAIL_PORT', cast=int)   # برای دریافت اجباری عدد

ALLOWED_HOSTS=localhost, 127.0.0.1, pylinux.ir