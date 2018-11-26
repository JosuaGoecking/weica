#!/usr/local/bin/bash                                                                                                                                                              

###############################################################################
#                                                                             #
#    Program name:   change_recipe.sh                                         #
#    Purpose:        Get the wanted changes in the recipe and commit them     #
#                    to the Python script for processing.                     #
#									      #
#    Author:         Josua Goecking                                           #
#    GitHub:         https://github.com/JosuaGoecking/weica                   #
#                                                                             #
###############################################################################

cd $WEICADIR

echo "Type in the name of the recipe you want to change."
read name

echo "Now type in the amount of change and the entry you want to change separated by a colon. Type 'stop' when you're finished."

ent=""
while true
do
    read entry
    if [ $entry == "stop" ]
    then
	break
    fi
    ent+=$entry
    ent+=";"
done

if [ -z $ent ]
then 
    ent="empty"
else
    ent=${ent::-1}
fi

echo "Do you want to change the preparation ('Zubereitung') also?"
read answer

if [ $answer == "yes" ]
then
    echo "Type in how to prepare the meal using only one string. To use paragraphs type § at the place where you want a paragraph."
    read prep
    prep=${prep// /_}
fi

if [ -z $prep ]
then
    prep="empty"
fi

$WEICA_EXE/change_recipe.py $WEICADIR $name $ent $prep
