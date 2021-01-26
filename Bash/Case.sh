#! /usr/bin/bash

book=$1

case $book in
    "harrypoter" )
        echo "Price of this $book is 300 Rs.";;
    "Feluda" )
        echo "Price of this $book is 250 Rs.";;
    "Sherlok Holmes" )
        echo "Price of this $book is 500 Rs.";;
    * )
        echo "Do not find.";;


esac