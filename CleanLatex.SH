#!/bin/bash 

#Ask the user for their  file name 

echo "Please type out your file name (case sensative, exclude file extension):"

read filename 

echo Please confirm that your filename is $filename [Y/N]

read answer 

if [ "$answer" == Y ]
then
	rm $filename.log || echo "We did not find a .log file"
	rm $filename.aux || echo "We did not find a .aux file"
	echo "We removed all the extra files from your LaTex document creation"
fi

if [ "$answer" == N ]
then
        echo "Sorry, looks like you typed it wrong then. Try rerunning the script" 
fi
 

if [ "$answer" != N ] && [ "$answer" != Y ]
then
        echo "Sorry, looks like you didn't enter Y or N. Please re run the script"
fi
