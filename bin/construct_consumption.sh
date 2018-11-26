#!/usr/local/bin/bash    

###############################################################################
#                                                                             #
#    Program name:   construct_consumption.sh                                 #
#    Purpose:        Read in the consumption and commit it to the Python      #
#                    script for processing.                                   #
#                                                                             # 
#    Author:         Josua Goecking                                           #
#    GitHub:         https://github.com/JosuaGoecking/weica                   #
#                                                                             #
###############################################################################

cd $WEICADIR

del=0
echo "Reset consumption entries?"
read answer
if [ $answer == "yes" ]
then
    del=1
fi

echo "Type in the meals (recipes) or individual ingredients you consumed today. For recipes start with its name followed by optional changes, separated by a colon. For individual ingredients start with the amount followed by the ingredient, separated by a colon. Type in 'stop' when finished."
add=""
rec=""
while true
do
    read entry
    if [ $entry == "stop" ]
    then
	break
    elif [[ $entry =~ ^[0-9] ]]
    then
	add+=$entry
	add+=":"
    else
	rec+=$entry
	rec+=";"
    fi
done

if [ -z $rec ]
then
    rec="empty"
else
    rec=${rec::-1}
fi

if [ -z $add ]
then
    add="empty"
else
    add=${add::-1}
fi

$WEICA_EXE/add_consumption_script.py $WEICADIR $rec $add $del
