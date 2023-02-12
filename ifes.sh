touch ifes.sh

nano ifes.sh

#!/bin/bash

if (( $1 >= 0  ))
then
echo "$1 положительное"
else
echo "$1 отрицательное"
fi
./ifes 3



#!/bin/bash

mydir= /home/tanya/ifes.sh
if [ -d $ifes.sh ]
then
echo "The $ifes.sh directory exists"
cd $ifes.sh
ls
else
echo "The $ifes.sh directory does not exists"
fi
./ifes

