#!/usr/local/bin/bash                                                                                                                                                              
cd $WEICA_EXE

if [ -z $1 ]
then
    echo "Please specify type you want to add."
    exit -1
fi

case $1 in
    "consumption" )
	./construct_consumption.sh
	;;
    "dict" )
	./add_dict_entry.sh
	;;
    "recipe" )
	./construct_recipe.sh
	;;
    * )
	echo "Type $1 does not exist."
	;;
esac
