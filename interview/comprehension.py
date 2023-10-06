### List Comprehension
## with out list comprehension print number which are divisible by 3
ls=[]
for i in range(100):
    if i%3==0:
        ls.append(i)
print(ls)

## using list comprehension
'''syntax > [return-value for-loop if-condition]'''

ls=[i for i in range(100) if i%3==0]
print(ls)


### Dictionary Comprehension
'''syntax > {return-value for-loop if-condition}'''

dict1={i:f"item{i}" for i in range(100)}
print(dict1)



## Mapping & Filter

def main():
    
    even=[2,4,6,8,10,12,16,200]
    odd=[1,3,5,7,9,13,15,17,19]
    
    '''mapping'''
    
    evenSq = list(map(lambda e: e**2,even))
    print(evenSq,"evenSq")
    
    '''mapping and filter(print only even>4 and even<16)'''
    
    evenSquare = list(map(lambda e: e**2,(filter(lambda e:e>4 and e<16,even))))
    print(evenSquare,"evenSquare")
    
    '''this will print the same result as above lines using list comprehension'''
    oddSq = [i**2 for i in odd]
    print(oddSq,"oddSq")
    
if __name__=="__main__":
    main()