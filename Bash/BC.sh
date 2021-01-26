#! /usr/bin/bash
num=25.5
num1=2

echo "25.5+2" | bc
echo "25.5-2" | bc
echo "25.5*2" | bc
echo "25.5/2" | bc

num=16

echo "scale=2;sqrt(4)" | bc
echo "scale=2;($num)^2" | bc