#!/usr/local/bin/bash                                                                                                                                                              

###############################################################################
#                                                                             #
#    Program name:   change.sh                                                #
#    Purpose:        Call the respective shell scripts to change certain      #
#                    data.                                                    #
#									      #
#    Author:         Josua Goecking                                           #
#    GitHub:         https://github.com/JosuaGoecking/weica                   #
#                                                                             #
###############################################################################

cd $WEICA_EXE

if [ -z $1 ]
then
    echo "Please specify the type you want to change."
    exit -1
fi

case $1 in
    "consumption" )
	./change_consumption_entry.sh
	;;
    "user_data" )
	./change_user_data.sh
	;;
    "PAL" )
	./change_PAL_value.sh
	;;
    "recipe" )
	./change_recipe.sh
	;;
    * )
	echo "Type $1 does not exist."
	;;
esac


    
