# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific aliases and functions
# source ./.myrc
#My alias values
#notes: \!* tells system to append any arguments at runtime
if [ -f ${HOME}/.dir_colors ]; then
eval `dircolors -b ~/.dir_colors`
fi

alias lsa='ls -la'
alias lsc='ls | grep -c cpp'
alias lsj='ls | grep -c java'
alias h=history
alias m=more
alias s=source
alias lls='ls -1F'
alias up='cd ..'
alias lo=logout
#alias gd='grep  Date *.sh  | grep 0600'
#alias gd='grep  Date *.sh  | grep 0500'
PATH=$PATH:$bin:.
alias vi='vim'
alias jc='javac *.java -d .'
#alias us='unshar'

