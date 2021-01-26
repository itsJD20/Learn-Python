echo -e "Enter the file name: \c"
read filenm

if [ -f $filenm ]
then
    if [ -w $filenm ]
    then
        echo "write some text and press ctrl+d to quit"
        cat >> $filenm
    else
        echo "do not have write permission"
    fi
else
    echo "Sorry no file $filenm"
fi