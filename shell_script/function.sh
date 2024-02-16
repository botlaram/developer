#!/bin/bash

#example : 1 (simple function)
intial_function() {
    echo "hello world"
}

intial_function


#example : 2 (pass user input)
NAME=$1

user_input() {
    echo "I'm the user-input $1"     #$1 will print input given by user
    echo "Script name : $0"          #$0 will print script name
    echo "number of arguments : $#"  #$# will print number of arguments passed to function
}

user_input $1 #to make use of arguments in fucntion, we need to pass argument while calling function 



#example : 3
#install package

verify_user() {
    if [ $(id -u) -eq 0 ]; then
        apt-get update
    else
        exit 1   #exit script if not root user
    fi
}
verify_user