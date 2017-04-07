#! /bin/bash

#----------------------------------
# $Author: ee364g15 $
# $Date: 2017-02-15 16:11:07 -0500 (Wed, 15 Feb 2017) $
#----------------------------------

function part_a 
{               
    python3.4 prelab.py 2> output.txt
    return                      
}                               

function part_b
{              


    return                     
}                              

function part_c
{
    arr=$(ls | grep *.c)
    echo "$arr"
    gcc ${arr[0]} 2> temp
    chk=$(head -n 1 ./temp | tail -n 1 | wc -w)
    x=0
    if [ "$chk" == "0" ]
    then 
	echo "${arr[0]}: success"
    else 
	echo "${arr[0]}: failure"
    fi
    rm temp
    return
}

function part_d
{
    Arr=(a.txt b.txt c.txt d.txt)
    (( rand = $RANDOM % 4 ))
    chk=$(head -n 6 ./${Arr[rand]} | tail -n 3)
    echo "$chk"
    return
}

function part_e
{
    line=$(ping -c 3 ecegrid.ecn.purdue.edu)
    chk=$(echo "$line" | head -n 8 | tail -n 1 | cut -d'/' -f 5)
    echo "$chk ms"
    return
}

# To test your function, you can call it below like this:
#

