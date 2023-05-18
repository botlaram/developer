##args
def sum(*args):
    """_summary_
    """
    total=0
    for i in args:
        total=total+i
    print(total)
    
sum(5,6,7,8,9)   ##we can pass n numbers of arguments

print("\n << eg 2 >> \n")
#================================================================
#eg2

def add_list(*args):
    """doc
    """
    list=[]
    for name in args:
        list.append(name)
        print(list,"\n")
    
add_list("ram","krishna","botla")

##for key words arguments 

def student(**data):
    for key,value in data.items():
        print(key,value,"\n")
        
##callable=student(key=value)
student(name="ram",id=5502209)
student(name="hari",id=5509902)