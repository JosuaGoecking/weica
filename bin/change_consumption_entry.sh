#!/usr/local/bin/bash                                                                                                                                                              
cd $WEICADIR

echo "Which entry do you want to change by which amount? Type first the entry followed by the amount of change separated by a colon."
read entry
echo "Do you want to add or multiply it?"
read mode

$WEICA_EXE/change_consumption_entry.py $WEICADIR $entry $mode
