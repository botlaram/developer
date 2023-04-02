##to read write the file 
##syntax > open("filepath","filemode")

f = open("./read_write_demo.txt","r")  ##r=read
print(f.read())   ##read() to print the txt 
f.close() ##close

print("\n << eg 2 >> \n")
#======================================================================================================
#eg 2   

##count the number of lines

f = open("./read_write_demo.txt","r")
count=0
for lines in f:
    print(str(count) + "  " + lines)
    count+=1
f.close()

print("\n << eg 3 >> \n")
#======================================================================================================
#eg 3 

##count only number of Males for txt file

f = open("./read_write_demo.txt","r")
count=0
for lines in f:
    if "M" in lines:
        print(str(count) + "  " + lines)
        count+=1

##usign list comprehension
male = list(line for line in f if "M" in line)  
print(male)
f.close()

print("\n << eg 4 write files >> \n")
#======================================================================================================
#eg 4 

##write file
f = open("./read_write_demo.txt","r")
create_male_file = open("./create_male_demo.txt","w")   ##createing file to add all Males for read_write_demo
create_female_file = open("./create_female_demo.txt","w")   ##createing file to add all Females for read_write_demo
for lines in f:
    if "M" in lines:
        create_male_file.write(lines)    ##adding file to new file
    else:
        create_female_file.write(lines)
f.close()
create_male_file.close()
create_female_file.close()