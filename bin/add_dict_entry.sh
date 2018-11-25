#!/usr/local/bin/bash
cd $WEICADIR

echo "Which entry do you want to add to the calory dictionary?"
read entry

echo "How many calories does this food contain per which amount? Type both calories and amount separated by a colon."
read data

$WEICA_EXE/add_dict_entry.py $WEICADIR $entry $data
