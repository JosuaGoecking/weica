#!/usr/local/bin/bash                                                                                                                                                              

###############################################################################
#                                                                             #
#    Program name:   compute_consumption.sh                                   #
#    Purpose:        Call the Python script to compute the consumption.       #
#                                                                             #
#    Author:         Josua Goecking                                           #
#    GitHub:         https://github.com/JosuaGoecking/weica                   #
#                                                                             #
###############################################################################i

cd $WEICADIR

$WEICA_EXE/compute_consumption.py $WEICADIR
