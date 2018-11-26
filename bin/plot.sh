#!/usr/local/bin/bash

###############################################################################
#                                                                             #
#    Program name:   plot.sh                                                  #
#    Purpose:        Get data and call the corresponding plotting Python      #
#                    scripts.                                                 #
#                                                                             #
#    Author:         Josua Goecking                                           #
#    GitHub:         https://github.com/JosuaGoecking/weica                   #
#                                                                             #
###############################################################################

cd $WEICADIR

if [ -z $1 ]
then
    echo "Please set variable to what you want to plot."
    exit -1
fi

show=0
echo "Show $1?"
read answer
if [ $answer == yes ]
then
    show=1
fi

$WEICA_EXE/plot_$1.py $WEICADIR $show

 
