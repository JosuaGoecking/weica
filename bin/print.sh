#!/usr/local/bin/bash                                                                                                                                                              
cd $WEICADIR

if [ -z $1 ]
then
    echo "Please set variable to what you want to print."
    exit -1
fi

ent=""
if [ $1 == "dict" ]
then
    echo "Do you want to specify the entries to print?"
    read answer
    if [ $answer == "yes" ]
    then
	echo "Type in the entries you want to print out. Type 'stop' when you're finished."
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
	ent=${ent::-1}
    fi
fi

if [ $1 == "recipe" ]
then
    echo "Type in recipe name."
    read ent
fi

$WEICA_EXE/print_$1.py $WEICADIR $ent
