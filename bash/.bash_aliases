# shellcheck disable=SC2148
# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

alias lsd='exa -lh --tree --git | tte burn'
alias lsdt='tree -lh | tte slide'

alias ,ls='exa --git-ignore -lh --tree ../AGENT'

### MY CURRENT BABY
function a() {
    cd ~/AGENT/
    source ./.venv/bin/activate
    exa -lh --tree --git
}
#################

function q() {
    cd ~/VSCODE_PROJECTS/songs/
#     source ~/PYCHARM_PROJECTS/my_chat_api_playground/.venv/bin/activate
}


alias ,c='clear'
alias ,..='cd ..'
alias ,...='cd ..; cd ..'
alias ,....='cd ..; cd ..; cd ..'
alias ,~='cd ~'

alias ,o='xdg-open .'

alias ,f="find . -maxdepth 1 -type d -print | xargs du -sk | sort -rn"

# apt
function ,au(){
    sudo apt update
    sudo apt upgrade
}
alias ,al='sudo apt list | grep'
alias ,as='sudo apt list --installed | grep'
alias ,ae='sudo nano /etc/apt/sources.list'

# git
alias ,gsshclone='echo "git clone ssh://git@github.com/dillonchaffey/<repository name>.git"'
alias gs='git status'
alias ,gs='git status'
alias ,gd='git diff'
function ,gc(){
    git commit -m "_"
    git push
}

alias p='python'
alias ,p='python'
alias ,pyweb='python3 -m http.server 9000'
alias ,vc='python3 -m venv ./venv'
alias ,va='source ./.venv/bin/activate'
alias ,vd='deactivate'

alias ,f='fuck'
alias ,su='sudo $(history -p !!)'

#'command | pbcopy' and then Ctrl-V elsewhere
alias pbcopy='xclip -selection clipboard'
alias pbpaste='xclip -selection clipboard -o'

alias ,br='source ~/.bashrc'
alias ,bb='cp ~/.bash_aliases ~/.bash_aliases.backup_$(date +%Y-%m-%d_%H%M%S)'
alias ,ba='kate ~/.bash_aliases'
alias ,brc='kate ~/.bashrc'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

PrintMotd() {
#     myvar=$(sed "/^## $1$/,/^## Heading/!d;//d;/^$/d" "/home/zakalwe/D-MONEY-TERMINAL/Notes/TodoToday/Todo_Today.md")
#     echo $myvar
headings_list=($(python3 -c 'import markdown, re; with open("/home/zakalwe/D-MONEY-TERMINAL/Notes/TodoToday/Todo_Today.md", "r") as f: markdown_text = f.read(); html_content = markdown.markdown(markdown_text); headings = re.findall(r"<h1>(.*?)</h1>", html_content); print(" ".join(headings))'))
echo $headings_list
}

## https://news.ycombinator.com/item?id=40503202
# printssh() {
#     tte --input-file YOUR_FILE --frame-rate=500 $(echo "beams binarypath blackhole bouncyballs bubbles burn colorshift crumble decrypt errorcorrect expand fireworks middleout     orbittingvolley overflow pour print rain randomsequence rings scattered slice slide spotlights spray swarm synthgrid unstable vhstape waves wipe" | tr ' ' '\n' | shuf -n 1)
#     ssh "$@"
# }
# alias ssh="printssh"
