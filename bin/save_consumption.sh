#!/usr/local/bin/bash                                                                                                                                                              

###############################################################################
#                                                                             #
#    Program name:   save_consumption.sh                                      #
#    Purpose:        Read in data and commit it to the Python script to       #
#                    save the consumption.                                    #
#                                                                             #
#    Author:         Josua Goecking                                           #
#    GitHub:         https://github.com/JosuaGoecking/weica                   #
#                                                                             #
###############################################################################

cd $WEICADIR

echo "Do you want to save the current consumption?"
read answer

if [ $answer != "yes" ]
then
    exit -1
fi

echo "Is it today's consumption?"
read answer

if [ $answer != "yes" ]
then
    echo "Type date of the day to whom this consumption belongs using the format YYYYMMDD."
    read date
fi

if [ -z $date ]
then
    date="empty"
fi

$WEICA_EXE/save_consumption.py $WEICADIR $date

