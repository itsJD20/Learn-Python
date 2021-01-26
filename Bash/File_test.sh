#! /usr/bin/bash
echo -e "enter th name: \c"
read file_name

if [ -d $file_name  ]
then
    echo "Hello file $file_name"
else
    echo "Bye file $file_name"
fi