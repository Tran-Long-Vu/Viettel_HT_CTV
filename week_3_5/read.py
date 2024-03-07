# Api script for postGRESQL.
# ORM translates python to SQL queries. 

# Import

# Credenials to connect

# Session define

# API query

# Run Server

# ... 

# Credentials
POSTGRES_USER="postgres"
POSTGRES_PASSWORD=1
POSTGRES_SERVER="localhost"
POSTGRES_PORT=5432
POSTGRES_DB="test"

import psycopg2

mydb = psycopg2.connect(
  host=POSTGRES_SERVER,
  user=POSTGRES_USER,
  password=POSTGRES_PASSWORD,
  database=POSTGRES_DB
)

mycursor = mydb.cursor()

mydb.set_session(autocommit=True)

#
#mycursor.execute('''CREATE TABLE employee(  
#      EmployeeID int,  
#      Name varchar(255),  
#      Email varchar(255));
#''')
#


# read one line to check
mycursor.execute('''SELECT * 
                 FROM customers 
                 WHERE id = 5;''')

# read to check
# mycursor.execute("SELECT * FROM customers")


# TODO: update -delete
print(mycursor.fetchall())

mycursor.close()
mydb.close()