#! /usr/bin/bash
n=1

while (( $n < 3 ))
do
    echo $n
    #n=$((n+1))
    ((n++))
    #((--n))
    #sleep 2
    #gnome-terminal &
    xterm &
done