#!/usr/local/bin/bash                                                                                                                                                             

###############################################################################
#                                                                             #
#    Program name:   change_PAL_value.sh                                      #
#    Purpose:        Get the hours of work, sleep and free time each with     #
#                    corresponding intensity and commit it to the Python      #
#		     script for processing.                  		      #
#									      #
#    Author:         Josua Goecking                                           #
#    GitHub:         https://github.com/JosuaGoecking/weica                   #
#                                                                             #
###############################################################################

cd $WEICADIR

echo "How many hours do you sleep per day?"
read sleep

cat $WEICADIR/data/PAL_values.txt
echo ""
echo "How many hours do you work per day and at which intensity (see table above)? Type the hours followed by the intensity separated by a colon."
read work

echo "How many free time do you have per day at which intensity? Type hours followed by the intensity separated by a colon."
read free

$WEICA_EXE/change_PAL_value.py $WEICADIR $sleep $work $free
