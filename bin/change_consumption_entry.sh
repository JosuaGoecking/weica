#!/usr/local/bin/bash                                                                                                                                                              

###############################################################################
#                                                                             #
#    Program name:   change_consumption_entry.sh                              #
#    Purpose:        Get the wanted change in the consumption and commit it   #
#                    to the Python script for processing.                     #
#									      #
#    Author:         Josua Goecking                                           #
#    GitHub:         https://github.com/JosuaGoecking/weica                   #
#                                                                             #
###############################################################################

cd $WEICADIR

echo "Which entry do you want to change by which amount? Type first the entry followed by the amount of change separated by a colon."
read entry
echo "Do you want to add or multiply it?"
read mode

$WEICA_EXE/change_consumption_entry.py $WEICADIR $entry $mode
