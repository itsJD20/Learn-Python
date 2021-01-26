#! /usr/bin/bash

echo -e "Enter : \c"
read book

case $book in
    [a-z] )
        echo "Name start with this alpha is $book  small";;
    [A-Z] )
        echo "Name start with this alpha is $book capital";;
    [0-9] )
        echo "Name start with this alpha is $book number";;
    ? )
        echo "This is special Character $book";;


esac

