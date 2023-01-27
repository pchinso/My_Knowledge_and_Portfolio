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

# Accessing Values

echo $NAME

# Read-only Variables

NAME="pChinso"
readonly NAME # After a variable is marked read-only, its value cannot be changed.

# Unsetting Variables to remove the variable from the list of variables
unset NAME

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


# to continue https://www.tutorialspoint.com/unix/unix-special-variables.htm

