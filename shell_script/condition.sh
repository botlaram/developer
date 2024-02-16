#!/bin/bash

#example : 1
check_status=$(id -u)  #output will be 0 for root user (root user id will be always 0)

if [ $check_status -eq 0 ]; then
    echo "I'm root user"
fi

if [ $check_status -ne 0 ]; then
    echo "not a root user, cannot install packages"
    exit 1     #this exit the script if error occurs
fi


#example : 2

if [ $? -eq 0 ]; then     #($? will be 0, if above condition execute successfully)
    apt-get install nano
fi

#example : 3

echo "Enter number : "
read number

#check if the input is greater then 0
if [ $number -gt 0 ]; then
    echo "given input is positive number"
#check if the input is lesser then 0
elif [ $number -lt 0 ]; then
    echo "given input is negative number"
else
    echo "not a valid number"
fi