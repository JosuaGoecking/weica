#!/usr/local/bin/bash

###############################################################################
#                                                                             #
#    Program name:   construct_recipe.sh                                      #
#    Purpose:        Read in the recipe data and commit it to the Python      #
#                    script for processing.                                   #
#                                                                             #
#    Author:         Josua Goecking                                           #
#    GitHub:         https://github.com/JosuaGoecking/weica                   #
#                                                                             #
###############################################################################

cd $WEICADIR

echo "Type in Name of the recipe."
read name
name_scored=${name// /_}
check="$(ls data/recipes/ | grep $name_scored)"

if [ ${#check} -gt 0 ]
then
    echo "Recipe with name '$name' already exists. Do you want to replace it?"
    read answer
    if [ $answer != "yes" ]
    then
	exit -1
    fi
fi

echo "How many portions are designated for this recipe?"
read portions

echo "Now type in the ingredients starting with the amount followed by a colon and then the kind. Type 'stop' when you're finished."
data=""

while true
do
    read ing
    if [ $ing == "stop" ]
    then
	break
    fi
    data+=$ing
    data+=";"
done

data=${data::-1}

echo "Any spices?"
read answer

if [ $answer == "yes" ]
then
    echo "Type them in as one string."
    read spices
    spices=${spices// /_}
fi

if [ ${#spices} -eq 0 ]
then
    spices=""
fi

echo "Now type in how to prepare the meal using only one string. To use paragraphs type § at the place where you want a paragraph."
read preparation
preparation=${preparation// /_}

meta="Name:$name_scored;Portionen:$portions;Gewürze:$spices;Zubereitung:$preparation" 

$WEICA_EXE/add_recipe_script.py $WEICADIR $meta $data
