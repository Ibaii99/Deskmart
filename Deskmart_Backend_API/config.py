
#Flask server principal attributes
HOST = '0.0.0.0'
PORT = 3000
API_URL_PREFIX= "/api/v1"
#Finnhub conexion
FINNHUB_API_KEY = "bugqbd748v6vml4hv8gg"
FINNHUB_SANDBOX_API_KEY = "sandbox_bugqbd748v6vml4hv8h0"
#INFLUXDB TOKEN
INFLUXDB_TOKEN = "6QCOt656axj-tWsEeTmZZ_URFB0ASrib1NZ0uGpqjuw-1ygd4xUeZzHhYHEkvt6y-wuERAY9ZYHFBsLCVHyw3Q=="
#MongoDB credentials
# MONGO_PORT = 27017
# MONGO_HOST = "localhost:" +  MONGO_PORT
# MONGO_USER = 'root'
# MONGO_PASS = 'root'
# MONGO_AUTHENTICATE_DB = "admin"

MONGO_HOST = "cluster0.fg8js.mongodb.net"
MONGO_PORT = 27017
MONGO_USER = 'udbank'
MONGO_PASS = '1qwerty78'
MONGO_AUTHENTICATE_DB = "udbank?retryWrites=true&w=majority"
#JWT
JWT_SIGN_KEY = "secret"
#HASH
SALT=b'\\a\xb9?\xa8P\xc6h\x85\xed)L\xa6\x99e\x0f\x86\xcf\xe8{2W\xc2\x17:\x1bR\xf8\x1b:\x88b'
#OPENWEATHER
OWM_APIKEY="cc79508fd2022eb4068c9f0dde04e3c7"