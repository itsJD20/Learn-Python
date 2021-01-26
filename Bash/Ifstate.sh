#! /usr/bin/bash
echo "Enter the number: "
read count

if [ $count = 1 ]
then
    echo "I love you"
elif [ $count = 4 ] 
then
    echo "bhag"
else
    echo "I hate you"
fi
