touch fors.sh

nano fors.sh

#!/bin/bash

for i in {1..11}
do [[  $((  $i % 2  )) -eq 0  ]]
echo $i
done