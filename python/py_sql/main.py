import mysql.connector
mydb= mysql.connector.connect(
    host='localhost',
    password="Ram@1234",
    user="root",
    database="demodb")  # database name needs to be added after creating db file name

# check database connection
if mydb.is_connected():
    print("Connection Successful")

mycursor=mydb.cursor()

# mycursor.execute("CREATE DATABASE demodb")   #create db


# mycursor.execute("SHOW DATABASES")   #show db files
# for db in mycursor:
#     print(db)


# mycursor.execute("CREATE TABLE students (name VARCHAR(250), age INTEGER(10))")  # create table

# mycursor.execute("SHOW TABLES")   # show tables
# for tb in mycursor:
#     print(tb)


# insert rows/data

# sqlFormula = "INSERT INTO students (name,age) VALUES (%s,%s)" #%s is place holders
# student1=("Ram",26)   # inputs
# mycursor.execute(sqlFormula,student1)  # insert in table
# mydb.commit()  # confirm the command

# insert multiple of data

# sqlFormula = "INSERT INTO students (name,age) VALUES (%s,%s)" #%s is place holders
# student=[("Ram",26),
#          ("Hari",24),
#          ("Swetha",24),
#          ("Rohini",48)]          # inputs
# mycursor.executemany(sqlFormula,student)  # use executemany insert multiple data in table
# mydb.commit()  # confirm the command


# get/select data

# mycursor.execute("SELECT * FROM students")   # selecting all data from table
# display_rows=mycursor.fetchall()   # fetches all the rows from table
# for rows in display_rows:
#     print(rows)
    
    
# fetch specific column

# mycursor.execute("SELECT age FROM students")   # selecting age data from table
# display_age=mycursor.fetchall()   # fetches age column from table   #fetchone is use to fetch only one data
# for age in display_age:
#     print(age)
    


