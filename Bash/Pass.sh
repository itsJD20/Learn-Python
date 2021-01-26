#! /usr/bin/bash

echo $0 $1 $2 $3 '> echo $1 $2 $3'

arg=("$@")
#echo "the names: " ${arg[0]}, ${arg[1]}, ${arg[2]}

echo "hello!" $@
echo " numbers: " $# 