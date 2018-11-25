#!/usr/local/bin/bash  
cd $WEICADIR

echo "Type in the user data entry you want to change followed by the new value, separated by a colon. Type in 'stop' when finished."
ch=""
while true
do
    read change
    if [ $change == "stop" ]
    then
	break
    fi
    ch+=$change
    ch+=";"
done

ch=${ch::-1}

$WEICA_EXE/change_user_data.py $WEICADIR $ch
