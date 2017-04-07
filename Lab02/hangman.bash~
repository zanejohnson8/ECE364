#! /bin/bash

#---------------------------------------
# $Author: ee364g15 $
# $Date: 2017-01-25 17:24:13 -0500 (Wed, 25 Jan 2017) $
#---------------------------------------

# Do not modify above this line.

word1=(b a n a n a)
word2=(p a r s i m o n i o u s)
word3=(s e s q u i p e d a l i a n)
answer=(                    );
arr=(banana parsimonious sesquipedalian)
(( elem=$RANDOM % 3 ))

len=$(echo "${arr[$elem]}" | wc -c )
(( len-- ))

if (( $elem == 0 )) 
then
	word=(b a n a n a)
elif (( $elem == 1 ))
then 
	word=(p a r s i m o n i o u s)
elif (( $elem == 2 )) 
then
	word=(s e s q u i p e d a l i a n)
fi 

echo "Your word is $len letters long."
complete=0
cor_cnt=0
final_cor_cnt=0
i=0

echo -n "Word is: "

while (( $i < $len ))
do
	echo -n ". "
	answer[$i]="."
	
	(( i=$i+1 ))
done 
i=0
echo ""
while (( complete == 0 ))
do 

	if (( $final_cor_cnt == (( $len )) ))
	then
		echo -n "Congratulations! You guessed the word: "
		while (( $i < $len ))
			do 
			echo -n "${word[$i]}"	
			(( i++ ))
			
			done
			echo ""
			i=0
		exit 0
	fi	
	echo -n "Make a guess: "
	read guess 
	echo ""
	
	while (( $i < $len ))
	do 
		
		if [ "$guess" == "${word[$i]}" ]
		then 
			(( cor_cnt=cor_cnt + 1 ))
		fi
		
		(( i++ ))	
	
	done


        if (( $cor_cnt > 0 )) 
	then
		echo -n "Good going! "
		
	else  
		echo -n "Sorry, try again. Word is: "
	fi 
	
	cor_cnt=0
	final_cor_cnt=0
	i=0

	while (( $i < $len ))
	do 
	
		
		if [ "$guess" == "${word[$i]}" ]
		then 
			answer[$i]=$guess			
		fi	
			
		(( i++ ))
	
	done
	i=0
	while (( $i < $len ))
	do 
		if [ "${answer[$i]}" == "${word[$i]}" ]
		then 
			(( final_cor_cnt=final_cor_cnt + 1 ))
		fi
		
		(( i++ ))
	
	done
	i=0

if (( $final_cor_cnt != $len ))
then
	echo -n "Word is: "
	while (( $i < $len ))
	do 
		echo -n "${answer[$i]} "	
		(( i++ ))
	
	done
	i=0
fi

	echo ""
done
exit 0
