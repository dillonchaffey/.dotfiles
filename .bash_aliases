alias c='clear'
alias ..='cd ..' 
alias ...='cd ..; cd ..'
alias ....='cd ..; cd ..; cd ..'

mcd(){ mkdir -p "$@" && cd "$@";} 

alias dc='cd ~/sbox/dillonchaffey/'

#APT
alias ai='sudo apt install'
alias al='sudo apt list | grep'
alias au='sudo apt update'

alias ls='ls -AlhF --color=auto'

alias diskspace="du -S | sort -n -r |more"
alias folders="find . -maxdepth 1 -type d -print | xargs du -sk | sort -rn"

alias p='python'
alias mact='python3 -m venv venv'
alias act='source venv/bin/activate'
alias pyweb='python3 -m http.server'

#GIT
alias gs='git status'
alias ga='git add . && git commit -am '
alias gp='git push origin master'

function g() {
    git add .
    git commit -a -m $*
	git push origin master
}

function gt() { { cd .git &> /dev/null && cd .. && git add -A && git commit -m "${1:-push`date`}" && git push; } || echo "WARNING! This is not a git folder."; }