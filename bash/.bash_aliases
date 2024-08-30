# shellcheck disable=SC2148
# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# alias bat='batcat'
alias nano='micro'
alias vim='micro'

alias lsd='exa -lh --tree --git | tte burn'
alias lsdt='tree -lh | tte slide'

alias lse="eza --color=always --long --git --no-filesize --icons=always --no-time --no-user --no-permissions"
alias ,ls='exa --git-ignore -lh --tree ../AGENT'

### MY CURRENT BABY
function a() {
    cd ~/AGENT/
    source ./.venv/bin/activate
    exa -lh --tree --git
}
#################

function q() {
    cd ~/A_GENT
    source ~/.my_venvs/A_GENT_venv/bin/activate
}
alias ,va='source ./.venv/bin/activate'

function s() {
    cd ~/VSCODE_PROJECTS/songs
}

alias ,tl='tmux list-sessions'
alias ,tk='tmux kill-server'
alias ,ta='tmux a'
alias ,td='tmux detach'
alias ,tc='tmux new-window'
# tmux new-session -d -s "foofoo"
# tmux new-window -n "fooooo"

alias ,weather='curl -m 1 wttr.in | tte rain'

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
# alias ,vc='python3 -m venv ./venv'
alias ,va='source ./.venv/bin/activate'
alias ,vd='deactivate'

alias ,f='fuck'
alias ,su='sudo $(history -p !!)'

#'command | pbcopy' and then Ctrl-V elsewhere
alias pbcopy='xclip -selection clipboard'
alias pbpaste='xclip -selection clipboard -o'

alias ,br='source ~/.bashrc'
alias ,brp='source ~/.profile'
alias ,bBACKUP_BASHALIASES='cp ~/.bash_aliases ~/.bash_aliases.backup_$(date +%Y-%m-%d_%H%M%S)'
alias ,bEDITALIASES='kate ~/.bash_aliases'
alias ,bEDITBASHRC='kate ~/.bashrc'
alias ,bEDITPROFILE='kate ~/.profile'
alias ,bEDITSOURCES='sudo nano /etc/apt/sources.list'

alias ,find_in_files_live="rg --line-number --with-filename . --color=always --field-match-separator ' ' | fzf --preview \"bat --color=always {1} --highlight-line {2}\" --preview-window ~8,+{2}-5"


# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'


show_file_or_dir_preview="if [ -d {} ]; then eza --tree --color=always {} | head -200; else bat -n --color=always --line-range :500 {}; fi"

export FZF_CTRL_T_OPTS="--preview '$show_file_or_dir_preview'"
export FZF_ALT_C_OPTS="--preview 'eza --tree --color=always {} | head -200'"

# Advanced customization of fzf options via _fzf_comprun function
# - The first argument to the function is the name of the command.
# - You should make sure to pass the rest of the arguments to fzf.
_fzf_comprun() {
  local command=$1
  shift

  case "$command" in
    cd)           fzf --preview 'eza --tree --color=always {} | head -200' "$@" ;;
    export|unset) fzf --preview "eval 'echo ${}'"         "$@" ;;
    ssh)          fzf --preview 'dig {}'                   "$@" ;;
    *)            fzf --preview "$show_file_or_dir_preview" "$@" ;;
  esac
}













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






