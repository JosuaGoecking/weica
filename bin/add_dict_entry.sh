#!/usr/local/bin/bash

###############################################################################
#                                                                             #
#    Program name:   add_dict_entry.sh                                        #
#    Purpose:        Get new dict entry and commit it to the python script    #
#		     for processing.                                          #
#									      #
#    Author:         Josua Goecking                                           #
#    GitHub:         https://github.com/JosuaGoecking/weica                   #
#                                                                             #
###############################################################################

cd $WEICADIR

echo "Which entry do you want to add to the calory dictionary?"
read entry

echo "How many calories does this food contain per which amount? Type both calories and amount separated by a colon."
read data

$WEICA_EXE/add_dict_entry.py $WEICADIR $entry $data
