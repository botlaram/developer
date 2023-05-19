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


## insert rows/data

# sqlFormula = "INSERT INTO students (name,age) VALUES (%s,%s)" #%s is place holders
# student1=("Ram",26)   # inputs
# mycursor.execute(sqlFormula,student1)  # insert in table
# mydb.commit()  # confirm the command

## insert multiple of data

# sqlFormula = "INSERT INTO students (name,age) VALUES (%s,%s)" #%s is place holders
# student=[("Ram",26),
#          ("Hari",24),
#          ("Swetha",24),
#          ("Rohini",48)]          # inputs
# mycursor.executemany(sqlFormula,student)  # use executemany insert multiple data in table
# mydb.commit()  # confirm the command


## Get/select data

# mycursor.execute("SELECT * FROM students")   # selecting all data from table
# display_rows=mycursor.fetchall()   # fetches all the rows from table
# for rows in display_rows:
#     print(rows)
    
    
## Fetch specific column

# mycursor.execute("SELECT age FROM students")   # selecting age data from table
# display_age=mycursor.fetchall()   # fetches age column from table   #fetchone is use to fetch only one data
# for age in display_age:
#     print(age)
    

## Fetch the data from value using where cmd

# sql= "SELECT * FROM students WHERE age=26"
# mycursor.execute(sql)

# display_values=mycursor.fetchall()

# for value in display_values:
    # print(value)

## Fetch data which looks like

# mycursor.execute("SELECT  * FROM students WHERE name LIKE 'Ra%'")
# # mycursor.execute("SELECT  * FROM students WHERE name LIKE '%we%'")  ## it will return the name with contain we
# display_values = mycursor.fetchall()

# for names in display_values:
#     print(names)

## Fetch data in desc order

# mycursor.execute("SELECT * FROM students ORDER BY name DESC")
# display_names=mycursor.fetchall()

# for names in display_names:
#     print(names)

## Fetch data in order

# mycursor.execute("SELECT * FROM students ORDER BY name") 
# display_order=mycursor.fetchall()
# for order_by in display_order:
#     print(order_by)
    
       
## update data 
# mycursor.execute("UPDATE students SET age=22 WHERE name='Swetha'")

## display limit values

# mycursor.execute("SELECT * FROM students LIMIT 4")
# display_names=mycursor.fetchall()
# for names in display_names:
#     print(names)


## delete data 

# mycursor.execute("DELETE FROM students WHERE name='Ram'")

## delete table 

mycursor.execute("DROP TABLE students")