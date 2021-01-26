echo -e "enter the number: \c"
read count
if [ $count -gt 1 ] || [ $count -eq 9 ]
then 
echo "matched"
else
echo "Not matched"
fi
--------------------------------------------

echo -e "enter the number: \c"
read count
if [ $count -gt 1 ] && [ $count -eq 9 ]
then 
echo "matched"
else
echo "Not matched"
fi