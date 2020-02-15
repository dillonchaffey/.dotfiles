alias c='clear'

function m {
  if [ ! -n "$1" ]; then
    echo "Enter a directory name"
  elif [ -d $1 ]; then
    echo "\`$1' already exists"
  else
    mkdir $1 && cd $1
  fi
}

#alias dc='cd ~/sbox/dillonchaffey/'
function dc() {
	if [ $# -eq 0 ]
	then
		cd ~/sbox/Flask_Leaflet/
		source venv/bin/activate
	elif [ $* = "1" ]
	then
		cd ~/sbox/dillonchaffey
		source venv/bin/activate
	else
		cd ~/sbox/$*
		source venv/bin/activate
	fi	
}

#APT
alias ai='sudo apt install'
alias ar='sudo apt remove'
alias aa='sudo apt autoremove'
alias al='sudo apt list | grep'
alias as='sudo apt list --installed | grep'
alias au='sudo apt-get update && sudo apt-get upgrade'

alias ae='sudo nano /etc/apt/sources.list'


alias ls='ls -AlhF --color=auto'

alias diskspace="du -S | sort -n -r |more"
alias folders="find . -maxdepth 1 -type d -print | xargs du -sk | sort -rn"

alias p='python'
alias mact='python3 -m venv venv'
alias act='source venv/bin/activate'
alias pyweb='python3 -m http.server'

#GIT
alias gs='git status'
alias ga='git add'
alias gp='git push origin master'

function g() {
    git add .
    git commit -a -m $*
	git push origin master
}

function gt() { { cd .git &> /dev/null && cd .. && git add -A && git commit -m "${1:-push`date`}" && git push; } || echo "WARNING! This is not a git folder."; }

#HEROKU
alias hl='heroku logs'
alias hp='git push heroku master'