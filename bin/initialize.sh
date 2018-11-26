#!/usr/local/bin/bash

###############################################################################
#                                                                             #
#    Program name:   initialize.sh                                            #
#    Purpose:        Read in the user data and commit it to the Python        #
#                    script for initializing weica.                           #
#                                                                             #
#    Author:         Josua Goecking                                           #
#    GitHub:         https://github.com/JosuaGoecking/weica                   #
#                                                                             #
###############################################################################

cd $WEICADIR

echo "This script will initialize your weica instance. You should run this when first using weica."
echo "Running this script will remove your calory dictionary, user data and your current consumption, if they already exist."
echo "Do you want to continue? [yes/no]"
read answer

if [ "$answer" != "yes" ]; then
    exit 1
fi

pars=("birthday" "gender" "weight" "height" "abdomen" "neck" "mode" "cal_demand")
desc=("[YYYYMMDD]" "[male/female]" "[kg]" "[cm]" "[cm]" "[cm]" "[lose/keep/gain]" "[formula/file]")

USER_DATA=""
for i in {0..7}
do
    echo -n "${pars[$i]} ${desc[$i]}: "
    read value
    USER_DATA+="${pars[$i]}:$value;"
done

USER_DATA=${USER_DATA::-1}

$WEICA_EXE/initialize.py $WEICADIR $USER_DATA
