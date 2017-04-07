#! /bin/bash

#---------------------------------------
# $Author: ee364g15 $
# $Date: 2017-01-18 16:32:15 -0500 (Wed, 18 Jan 2017) $
#---------------------------------------

# Do not modify above this line.

Num_Of_Param=$#
txtfiles=$@
cnt=$Num_Of_Param
i=2 
sum_=0
k=1
j=0
sel=0
tot_a=0
tot_m=0
max=0
arrtxt=($txtfiles)
sport=${arrtxt[1]}
log=${arrtxt[0]}
if (( cnt < 2 ))
then 
	echo "Usage: colect_stats.bash <file> <sport>"
	echo ""
	exit 1
fi

if [ ! -r $log ]
then
	echo "Error: $log does not exist"
	echo ""
	exit 2
fi

linecnt=$(wc -l < "./$log") 
while (( j < $linecnt ))
do
	t_sport=$(cut -d',' -f2 ./$log | head -n $k | tail -n 1)
	if [ $sport == $t_sport ]
	then
		cur_medal=$(cut -d',' -f3 ./$log | head -n $k | tail -n 1)
		(( tot_a=$tot_a+1 ))
		(( tot_m+=$cur_medal ))		
		if (( $cur_medal > $max ))
		then	
			max=$cur_medal
			name=$(cut -d',' -f1 ./$log | head -n $k | tail -n 1)
		fi		
	fi
	(( j=$j+1 ))
	(( k=$k+1 ))
done
echo "Total athletes: $tot_a"
echo "Total medals won: $tot_m"
echo "$name won the most medals: $max"
echo ""
exit 0


