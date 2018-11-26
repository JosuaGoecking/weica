
###############################################################################
#                                                                             #
#    Program name:   weica.sh                                                 #
#    Purpose:        Parse the given options and run the corresponding        #
#                    shell scripts, which will then in turn run the           #
#                    corresponding Python scripts.                            # 
#                                                                             #
#    Author:         Josua Goecking                                           #
#    GitHub:         https://github.com/JosuaGoecking/weica                   #
#                                                                             #
###############################################################################

weica () {

if [ -z $1 ]
then
    cat $WEICA_EXE/info.txt
    cat $WEICA_EXE/usage.txt
fi

OPTIND=1

while getopts "a:cg:hie:v:d:s?0" OPT
do
    case $OPT in
	"a" ) $WEICA_EXE/add.sh $OPTARG
	    ;;
	"c" ) $WEICA_EXE/compute_consumption.sh
	    ;;
	"g" ) $WEICA_EXE/plot.sh $OPTARG
	    ;;
	"h" ) cat $WEICA_EXE/info.txt 
	    cat $WEICA_EXE/usage.txt
	    ;;
	"i" ) cat $WEICA_EXE/info.txt
	    ;;
	"e" ) $WEICA_EXE/change.sh $OPTARG
	    ;;
	"v" ) $WEICA_EXE/print.sh $OPTARG
	    ;;
	"d" ) $WEICA_EXE/rm.sh $OPTARG
	    ;;
	"s" ) $WEICA_EXE/save_consumption.sh
	    ;;
	"?" ) cat $WEICA_EXE/usage.txt
	    ;;
        "0" ) $WEICA_EXE/initialize.sh
            ;;
	"*" ) cat $WEICA_EXE/usage.txt
	    ;;
    esac
done
}

_weica () {

    if [ ${#COMP_WORDS[@]} -gt 3 ]
    then
	return
    fi

    COMPREPLY=($(compgen -W "-a -e -c -d -g -v -s" "${COMP_WORDS[1]}"))
    
    case "${COMP_WORDS[1]}" in
	-a )
	    COMPREPLY=($(compgen -W "consumption dict recipe" "${COMP_WORDS[2]}"))
	    ;;
	-e )
	    COMPREPLY=($(compgen -W "consumption PAL recipe user_data" "${COMP_WORDS[2]}"))
	    ;;
	-g )
	    COMPREPLY=($(compgen -W "consumption BMI body_fat" "${COMP_WORDS[2]}"))
	    ;;
	-v ) 
	    COMPREPLY=($(compgen -W "cal_demand consumption dict recipe status user_data" "${COMP_WORDS[2]}"))
	    ;;
	-d )
	    COMPREPLY=($(compgen -W "consumption dict recipe" "${COMP_WORDS[2]}"))
	    ;;
    esac
}

complete -F _weica weica
