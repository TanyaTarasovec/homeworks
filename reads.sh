touch reads.sh

nano reads.sh

#!/bin/bash

echo "Введите число a:"
read a
if ((  $a >= 15  &&  $a <= 45  ))
then
echo "True"
else
echo "Error"
fi

#!/bin/bash

echo "Введите число b:"
read b
if ((  $b <= -1  &&  $b = 45 ))
then
echo "True"
else
echo "Error"
fi