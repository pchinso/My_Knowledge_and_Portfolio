#!/bin/sh

# Variable Names
# The name of a variable can contain only 
# letters (a to z or A to Z), 
# numbers ( 0 to 9) 
# or the underscore character ( _).

# By convention, Unix shell variables will have their names in 
# UPPERCASE.

# Defining Variables

NAME="pChinso"
NAMETOREMOVE = "Remove"

# Accessing Values

echo $NAME

# Read-only Variables

NAME="pChinso"
readonly NAME # After a variable is marked read-only, its value cannot be changed.

# Unsetting Variables to remove the variable from the list of variables
unset NAMETOREMOVE

# Variable Types

# Local Variables 
# A local variable is a variable that is present within the current instance of the shell. 
# It is not available to programs that are started by the shell. 
# They are set at the command prompt.

# Environment Variables 
# An environment variable is available to any child process of the shell. 
# Some programs need environment variables in order to function correctly. 
# Usually, a shell script defines only those environment variables that are needed by the programs that it runs.

# Shell Variables 
# A shell variable is a special variable 
# that is set by the shell and is required by the shell in order to function correctly. 
# Some of these variables are environment variables whereas others are local variables.

echo "# Shell Variables"

echo "For example, the $ character represents the process ID number, or PID, of the current shell: $$ "

echo "\$0 The filename of the current script. $0 "

echo -e "\$1 These variables correspond to the arguments with which a script was invoked." 
echo -e "Here n is a positive decimal number corresponding to the position of an argument \n(the first argument is $1, the second argument is $2, and so on)"
echo $n

echo "\$# The number of arguments supplied to a script. $# "

echo "\$* All the arguments are double quoted. If a script receives two arguments, \$* is equivalent to \$1 \$2: $*"

echo "\$@ All the arguments are individually double quoted. If a script receives two arguments, \$@ is equivalent to \$1 \$2 : $@" 

echo "\$? The exit status of the last command executed: $?" 

echo "\$$ The process number of the current shell. For shell scripts, this is the process ID under which they are executing: $$" 

echo "\$! The process number of the last background command. $!"


# to continue https://www.tutorialspoint.com/unix/unix-special-variables.htm
# Special Parameters $* and $@
