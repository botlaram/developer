---
hide:
  - navigation
  - tags
---
 
<h1></h1>

# Grab the Python stuff here ...😉

Usage doc is to state syntax for builtin funct. and modules

##Builtin or Modules

### args and kwargs

- In Python, we can pass a variable number of arguments to a function using special symbols. There are two special symbols:

1. *args (Non Keyword Arguments)

2. **kwargs (Keyword Arguments)

- We use ***args and **kwargs as an argument when we are unsure about the number of arguments to pass in the functions.

### magic methods

```
num=10
num + 5
15
num.__add__(5)  ##magic method __add__
15
```

click [here](https://www.tutorialsteacher.com/python/magic-methods-in-python) for more magic method

### isinstance

The isinstance() function returns True if the specified object is of the specified type, otherwise False
 
- syntax
```
isinstance(object, type)
```

### decorator

- decorators allow you to change the behavior of a function without modifying the function itself.
 
- syntax
```
def my_decorator_func(func):

    def wrapper_func():
        # Do something before the function.
        func()
        # Do something after the function.
    return wrapper_func

#using decoarate

@my_decorator_func
def my_func():
    pass

```

### Lambda

lambda basic form
 
- lambda (parameters):(return_Val)

- lambda x,y:x+y

Value will return automatically
 
![Lambda Syntax](./png/lambda_syn.png)

- lambda is used to avoid a small function
so that it can be placed in one line

### Filter
 
Filtering in python (which is similar to mapping)

- Syntax
```
filter(some_function,my_list)
```

![Filter eg](./png/filter_eg.png)

### Mapping

Mapping is to map the values with respt. parameters

- Syntax
```
map(some_function,my_list)
```

- for eg: mapping the dict. Key and vlaues
 
![Mapping Eg](./png/mapping_eg.png)

- Mapping is used by calling it on the List and passing it some function

![Mapping Eg](./png/mapping_eg2.png)

### List Comprehension
 
the simply readable way of transforming elements in list either by mapping or filtering
 
- List Comprehension Syntax for Mapping

```
var = class_type({return_value} {for loop})
```

- List Comprehension Syntax for Filtering

```
var = class_type({return_value} {for loop} {condition})
```
### read and write

- syntax
```
f = open({file_path},{file_mode})
```

### dataclass
 
- this module define classes that only act as data containers and when we do that, we spend a consequent amount of time writing boilerplate code with tons of arguments, an ugly __init__ method and many overridden functions.
 
- When you use dataclasses, you first have to import dataclass and then use it as a decorator before the class you define.

- syntax
```
from dataclasses import dataclass   ##import dataclass

@dataclass
class Book:

    title : str    ###variables are define without using __init__ instance
    author : str
    price : float

book=Book("title","author",price)
print(book.price)           ###print values
```
