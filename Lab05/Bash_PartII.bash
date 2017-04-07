#! /bin/bash

#----------------------------------
# $Author: ee364g15 $
# $Date: 2017-02-15 16:11:07 -0500 (Wed, 15 Feb 2017) $
#----------------------------------



Num_Of_Param=$#
txtfiles=$@
cnt=$Num_Of_Param
arrtext=($txtfiles)

if (( $cnt < 2 ))
then 
	echo "Usage: Bash_PartII.bash <file> <balance>"
	exit 2
fi


