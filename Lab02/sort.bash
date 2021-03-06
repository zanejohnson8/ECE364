#! /bin/bash

#---------------------------------------
# $Author: ee364g15 $
# $Date: 2017-01-25 16:19:50 -0500 (Wed, 25 Jan 2017) $
#---------------------------------------

# Do not modify above this line.

while getopts f:o:-: foo 2>/dev/null
do

    case $foo in

	f) 	in=$OPTARG	    
		;; #This means break

	o)	out=$OPTARG	    
		;;

	-) 	 
		 test=$(echo "$OPTARG" | cut -d"=" -f1 )
		 if [ $test == "column_number" ] 
		 then 
			x=1
		 else 
			echo "Invalid option."
			echo ""
			exit 2
		 fi 
		 cnum=$(echo "$OPTARG" | cut -d"=" -f2 )
	  	 ;;

	# The variable $foo gets set to '?' when an invalid option is supplied.
	\?) echo "Invalid option."
	    echo ""
	    exit 2
	    ;;

        # Default case
	*) echo "Default case."
	    ;;

    esac

done

	if [ ! -r ./$in ]
	then
		echo "Error: Input file $in is not readable."
		echo ""
		exit 3	
	fi


linenum=$(head -n1 ./$in | wc -w)

	if (( $cnum <= $linenum ))
	then
		echo "Sorting rows by column #$cnum."
		echo ""
		sort -k$cnum -n $in -o $out 
	else 
		echo "Error: Invalid column number."
		echo ""
	fi
exit 0
