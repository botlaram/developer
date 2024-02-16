#!/bin/bash

#in bash script, even some lines fail. Script cont. to execute further instead of throwing error
#we need to get exit status of function/command, to execute further script
#to check exit code > echo $?
#if $?= 0 (success) , $?=(1-127) (fail)

# user input 
echo -n "Enter Username : "  
read USERNAME

echo $USERNAME                  #display username
echo $?                         #display exit code (if exit code 0, means code executed successfully)



#write condition if command fails
ls -la ## this is success command

if [ $? -eq 0 ]; then         #($? will be 0, if above condition execute successfully)
    echo "command successfully executed"
fi


ls ll   ## this is failure command because ls ll is not valid command

if [ $? -ne 0 ]; then
    echo "invalid command"
    exit 1
fi

echo "exection completed"