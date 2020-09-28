
#!/bin/bash -i

history > UserHistory.txt

year=`date +%Y`

month=`date +%m`

day=`date +%d`

echo "The date this history was taken is: $month-$day-$year" >> UserHistory.txt
