## install sql 

https://www.youtube.com/watch?v=MhaH7o3lf4E   # follow link to with sql with windows

## mysql cheat commands

https://www.interviewbit.com/mysql-cheat-sheet/

## create database

> mycursor.execute("CREATE DATABASE demodb")   # demodb is database file name

## show created/available database

> mycursor.execute("SHOW DATABASES") # add for loop to display databases

## create table

> mycursor.execute("CREATE TABLE students (name VARCHAR(250), age INTEGER(10))")

> mycursor.execute("CREATE TABLE "tablename" ("col1_name" "type"(250), "col2_name" "type"(10))")

## show tables

> mycursor.execute("SHOW TABLES")   # add for loop to show tables

note: to display GUI , select Workbench Schema.

## insert rows/data

> sqlFormula = "INSERT INTO students (name,age) VALUES (%s,%s)" # %s is place holders

> student1=("Ram",26)   # inputs

> mycursor.execute(sqlFormula,student1)  # insert in table

> mydb.commit()  # confirm the command

## display data in workbench

> USE "demodb"  # demodb: db filename  

## show data inside tables

```
SELECT *
FROM students
```

note : students is table name here

## insert multiple of data

```
sqlFormula = "INSERT INTO students (name,age) VALUES (%s,%s)" #%s is place holders
student=[("Ram",26),
         ("Hari",24),
         ("Swetha",24),
         ("Rohini",48)]          # inputs in the form of array passing the values in tuples
mycursor.executemany(sqlFormula,student)  # use execute many inserting into table
mydb.commit()  # confirm the command
```
## Add New Column

> ALTER TABLE users ADD age VARCHAR(3);


## get/select fetch all the data

```
mycursor.execute("SELECT * FROM students")   # selecting all data from table
display_rows=mycursor.fetchall()   # fetches all the rows from table
for rows in display_rows:
    print(rows)
```

## fetch specific column

```
mycursor.execute("SELECT age FROM students")   # selecting age data from table
display_age=mycursor.fetchaone()   #fetchone is use to fetch only one data
for age in display_age:
    print(age)
```

## fetch data using where 

```
sql= "SELECT  * FROM students WHERE age=26"
mycursor.execute(sql)

display_values=mycursor.fetchall()

for value in display_values:
    print(value)
```

## fetch data which looks like

```
mycursor.execute("SELECT * FROM students WHERE name LIKE 'Ra%'")
mycursor.execute("SELECT  * FROM students WHERE name LIKE '%we%'")  ## it will return the name with contain "we"
display_values = mycursor.fetchall()


for names in display_values:
    print(names)
```

## fetch data in desc order
```
mycursor.execute("SELECT * FROM students ORDER BY name DESC")
display_names=mycursor.fetchall()

for names in display_names:
    print(names)
```
## fetch data in order
```
mycursor.execute("SELECT * FROM students ORDER BY name") 
display_order=mycursor.fetchall()
for order_by in display_order:
    print(order_by)
```

## Update data

mycursor.execute("UPDATE students SET age=22 WHERE name='Swetha'")  # use forloop to print values

## display limit values

mycursor.execute("SELECT * FROM students LIMIT 4")

## delete data inside tables

mycursor.execute("DELETE FROM students WHERE name='Ram'")

## Delete tables

mycursor.execute("DROP TABLE "table-name")