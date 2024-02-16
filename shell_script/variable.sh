#!/bin/bash

echo "hello world"        #print var

PERSON1=RAM               #assign var
PERSON2=HARI
PERSON3=$1                #assign runtime variable
PERSON4=$(echo "Alien")   #assgin command to var
DATE=$(date)              #display date

echo "hello I'm person1 :  ${PERSON1}"

echo "good morning from person2 : ${PERSON2}"

echo "hi from person3 : ${PERSON3}"

echo "I'm ${PERSON4}"

echo "Execution date : ${DATE}"


# user input 
echo -n "Enter Username : "  
read USERNAME

echo $USERNAME                  #display username

# user input secure
echo -n "Enter Password this is secure: "
read -s PASSWORD     #-s wont display input on screen