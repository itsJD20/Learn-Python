#! /usr/bin/bash

os=('nj' 'mk' 'mnb' 'tor')
os[4]='jou'
unset os[2]
echo  "${os[0]}"
echo  "${os[1]}"
echo  "${os[@]}"
echo  "${!os[@]}"
echo  "${#os[@]}"