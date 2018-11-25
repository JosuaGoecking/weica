#!/usr/local/bin/bash                                                                                                                                                              
cd $WEICADIR

if [ -z $1 ]
then
    echo "Please set variable to what you want to remove."
    exit -1
fi

ent=""
if [ $1 == "consumption" ] || [ $1 == "dict" ]
then
    echo "Type in food entry that you want to remove."
    if [ $1 == "consumption" ]
    then 
	echo "Type 'all' if you want to remove the whole consumption dictionary"
    fi
    read ent
elif [ $1 == "recipe" ]
then
    echo "Type in recipe name and food entry that you want to remove separated by a colon."
    read ent
fi

$WEICA_EXE/rm_$1_entry.py $WEICADIR $ent
