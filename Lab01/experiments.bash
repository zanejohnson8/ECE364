#! /bin/bash

#---------------------------------------
# $Author: ee364g15 $
# $Date: 2017-01-18 16:31:37 -0500 (Wed, 18 Jan 2017) $
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
arrtxt=($txtfiles)

if (( $cnt < 1 ))
then 
	echo "Usage: experiments.bash <input 1> [input 2] .. [input N]"
	echo ""
	exit 1
fi
while (( $sel < cnt ))
do

 	echo "${arrtxt[$sel]}:"
	if [ ! -r ${arrtxt[$sel]} ]
	then
	     echo "Filename \"${arrtxt[$sel]}\" is not readable."
	
	else
	linecnt=$(wc -l < "./${arrtxt[$sel]}") 
	while (( j < $linecnt ))
	do
		while (( i < 5 ))
		do

			next=$(cut -d' ' -f$i ./${arrtxt[$sel]} | head -n $k | tail -n 1)   
			(( sum_+=$next ))			
			(( i=$i+1 ))
		done
		name=$(cut -d' ' -f1 ./${arrtxt[$sel]}| head -n $k | tail -n 1)
		avg=$sum_
		(( avg/=3 ))		
		echo "$name $sum_ $avg"
		sum_=0
		avg=0
		i=2
		(( j=$j+1 ))
		(( k=$k+1 ))
	done
	fi
	k=1
	j=0
	(( sel=$sel+1 ))
	echo ""
done
exit 0



