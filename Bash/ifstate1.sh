#! /usr/bin/bash
echo "Enter the number: "
read word

if [[ $word > "abccccc" ]]
then
    echo "I love you"
elif [[ $word = "abc" ]]
then
    echo "bhag"
else
    echo "I hate you"
fi