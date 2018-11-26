# weica
The **WEI**ght **C**ontrol **A**ssistant (weica) is a program for computing and keeping track of your daily calory intake as well as monitoring your weight development.

## Pre-requisites
For the program to run successfully with all its features you need at least Python 3 and Bash 4. It is also possible to run this program using only Python in the Python Shell, however the simplifying features for putting in the data are written in Bash and can only be run with Bash 4 installed. 
Hopefully, in future versions of this program the dependency on Bash will be revoked.
The shell scripts in the bin folder were tested on a machine where Bash 4 is installed in the `/usr/local/bin` folder, which is why the shebang (first line in the skript, which starts with `#!`) has been set to this folder. Depending on where your Bash 4 version is installed you probably need to change this line.
You can to this by running the following command in your Bash shell:
```
$ sed -i '1 s/^.*$/#!\/path\/to\/bash/' /path/to/weica/bin/folder/*.sh 
```
Note that you need to escape the slash characters in the sed command with a backslash. Best practise is to test this command first without the `-i` flag first and check the output if it does what it is supposed to do.

## Installation
After you have updated the scripts to the settings on your machine it is suggested to add the following lines to your `~/.bashrc` or `~/.bash_profile` file:
```
# weica
export WEICADIR=path/to/weica/
export WEICA_EXE=$WEICADIR/bin/
source $WEICA_EXE/weica.sh
```
If you wish to name the exported variables differently you will also need to change those in all the shell scripts of the bin folder.
After setting these variables and sourcing them or starting a new shell session weica should be ready for use. You can test this by typing
```
$ weica
```
This should print out the weica banner followed by a detailed description of the usage.

## Initialize weica
Having successfully set up weica on your machine you can start by initializing weica by running the following command.
```
$ weica -0
```
This will start a script, which first will ask you if you want to continue, since this script should only be run when setting up weica. Since you intend to do this type `yes`. Here and everywhere else in the program where the script asks for a `[yes/no]` input, every input except for `yes` will be interpreted as `no`.
After typing `yes` the script will ask you for some personal information like your birthday, gender, weight and so on. You can change those parameters later, however to successfully initialize weica you need to initialize those values. Therefore, if you do not want to set them now, just give it some random values.

The last thing the initialization script will ask from you is in which way you want to get the calory demand (cal_demand). You can either do this by formula, which will use the Harris-Benedict formula to compute the calory demand and will substract/add 600 calories if you are in mode lose/gain. In each case the range will be 200 calories.
Alternatively you can specify the calory demand yourself. For this you need to create a file called `cal_demand.txt` in the data folder. This file has to be of the following structure:
```
#weight[kg]     lot_lose [kcal/day]             upt_lose [kcal/day]     lot_keep [kcal/day]     upt_keep [kcal/day]     lot_gain [kcal/day]   upt_gain [kcal/day]
```
Note the crucial `#` at the beginning of the first line. In the next line you will need to specify the calory demand for the respective weight. 

For initializing weica it is suggested to first choose formula as cal_demand. If you want to switch to specify the calory demand by file you can change this and other settings of your user data by running `weica -e user_data`.

If your initialization was successful weica should print out its banner followed by a print-out of your user data and your status, i.e. your body mass index and your body fat percentage, computed using the U.S. Navy formula.
Before the banner the initialization script should have printed out the message that the PAL (physical activity level) value was set to a default of 1.7. This value is needed for the computation of the calory demand.
It is best to modify this value to your individual one by running 
```
$ weica -e PAL
```
and following the steps of this script.

## The next steps
You should now be able to use weica for computing your daily calory consumption. This works such that you will specify what you have eaten using a calory dictionary, which specifies the calories at a given amount for each food.
For this of course you will first need to fill your calory dictionary. This is done by running
```
$ weica -a dict
```
and following the steps of this script.
To specify everything you have eaten on one day can become pretty tedious, especially if you do not eat finished products but prepare them yourself. Therefore, weica has the feature of using recipes for the calory computation.
You can add a new recipe by running
```
$ weica -a recipe
```
The script will lead you through the process of creating your own recipe. Please keep in mind that you should never use spaces in the name of the recipe. Best practise is to use underscores instead.
After having entered everything it should print out the recipe and also compute the calories which this recipe contains per portion, given that you have provided all the ingredients to the calory dictionary. Otherwise it will throw an error. In that case add the missing ingredients to the calory dictionary (`weica -a dict`) and print the recipe again using `weica -v recipe`.

Now you can add your first calory consumption. Type
```
$ weica -a consumption
```
Answer the first question with yes if you want to remove older consumption entries and no otherwise.
Now you can type in your consumption, by just calling the name of the recipe in case of recipes or by typing the amount and kind of food from the calory dictionary separated by a colon. For recipes you can also change the amount if you used more or less of some ingredient by adding them after the recipe name separated by colons. For example your input could look like this:
```
$ weica -a consumption
Reset consumption entries?
yes
Type in the meals (recipes) or individual ingredients you consumed today. For recipes start with its name followed by optional changes, separated by a colon. For individual ingredients start with the amount followed by the ingredient, separated by a colon. Type in 'stop' when finished.
mac_and_cheese:1:macaroni 
2:apple
1:banana
stop
```
This of course assumes that you have a recipe named mac_and_cheese with at least one ingredient being named macaroni and the calory dictionary consisting of at least the entries macaroni, apple and banana.
Note that the amount by which you factor the food always corresponds to the amount given in the calory dictionary (dictionary units, d.u.), i.e. if you saved the macaronis by specifying the calories per 100g the specification above (`1:macaroni`) will mean 100g of macaroni.
If your consumption input was successful, after typing stop you should get the computed sum of your calory consumption followed by your current calory range. Depending on how high your current consumption is the result will be colored black (below the range), green (in the lower part of the range), yellow (in the upper part of the range) and red (above the range).

At the end of the day you can save your consumption by running
```
$ weica -s 
```

## Further features
The section before showed the basic function of weica. You can also do some additional things using weica. For example it is possible to plot your consumption over time if you saved it regularly. For this type
```
$ weica -g consumption
```
You can specify if you want the plot to be shown. Alternatively you can also access the png file in the plots folder.

Unless you run weica in the keep mode it is desired that some of your user data, like the weight, abdomen and neck will change over time. You can add these changes by running `weica -e user_data`.
It is suggested to do this at least once a week, since about once a week those measures will be updated when saving the consumption.
You can, therefore, plot also the development in your body fat percentage and your BMI by typing 
```
$ weica -g body_fat # or
$ weica -g BMI
```

Also you might want to manipulate your consumption, dictionary or recipes. To do this simply type `weica -e` followed by the kind you want to change and follow the steps of the scripts.

More information about what can be done can be found out by running
```
$ weica -h
```
or, if you are familiar with Python, by studying the source code.

Have fun using weica to get control of your weight and don't forget to give a star if you enjoy using weica.

## To Do
Unfortunately some of the features of weica are only supported for male users yet. This includes the computation of the body fat percentage. It is planned to have this resolved asap.

In a broader scope it is planned to update weica such that Bash scripts won't be necessary anymore for running weica. Also importing weica for every command instead of importing it once not only costs more computation time but also should not be necessary.
The idea is to run weica such that it opens its own shell at which commands can be given (like e.g. `add consumption`), which then will read in the corresponding input without leaving the program.

Further it would be nice to change the implementation of the calory dictionary, since for larger dictionaries this will become more and more confusing. Categorizing each food should allow for a clearer structure. 
Another change to the dictionary should be the possibility to change between units.

It would be also nice if one could set up different weica users each one with its own user data. Easily changing between users and making their data only accessible to them would be a great feature.

Also there is improvement in the use of recipes. Allowing for them to be printed not only like it is implemented now but also in a prettier way, like a html or pdf file with picture could extent weica to not only being a tool for weight control but also for creating cook books.

Architecturally this could be done by separating weica into several classes, one user class, one dictionary class, one recipe classe and so on.

## Contribute
Contributions to this project are warmly welcome. You can either focus by the points specified in the to do list or if you have your own ideas to improve weica just implement them.
Best practise for contributing is the "Fork and pull" Git workflow:

1. **Fork** the repo on GitHub
2. **Clone** it to your own machine
3. **Commit** your changes to your branch
4. **Push** your changes to your fork
5. Submit a **Pull request** so your changes can be reviewed.
