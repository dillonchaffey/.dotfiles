#!/bin/bash

#make sure only one instance is running
[ "${FLOCKER}" != "$0" ] && exec env FLOCKER="$0" flock -en "$0" "$0" "$@" || :

if [ $EUID != 0 ]; then
    sudo "$0" "$@"
fi

readonly DEBUG=0

readonly VENV_PATH="/home/zakalwe/PYCHARM_PROJECTS/my_chat_api_playground/.venv/bin/python"
readonly HANDLE_KEY_SCRIPT="$VENV_PATH ./main.py"
# readonly HAND_ARROWKEY_SCRIPT="$VENV_PATH ./handle_arrow_keys.py"

 if ! command -v evtest &> /dev/null; then
     echo "evtest is not installed. Installing now..."
     apt-get update && apt-get install -y evtest
 fi

readonly MACRO_KBD_NAME="HP USB Keyboard" # bash evtest to get list of plugged in kbds
# Get the event number of the keyboard
keyboard_name=$(grep -Er "$MACRO_KBD_NAME" /sys/class/input/event*/device/name | sort -r)
event_number=$(echo $keyboard_name | cut -d'/' -f5 | cut -d':' -f2)

if ! evtest --grab "/dev/input/$event_number" | while read -r line; do
    if [[ $line == *"type 1 (EV_KEY), code "* ]]; then
        # Extract keycode and state
        keyname=$(echo $line | awk -F'code ' '{print $2}' | awk '{print $2}' | tr -d ',' |  sed 's/[()]//g')
        state=$(echo $line | awk '{print $NF}')

        if [[ $DEBUG -eq 1 ]]; then
            if [ $state -eq 1 ]; then
                echo "DEBUG: Key pressed: $keyname"
                continue
            fi
        fi

#        prev_rows=rows
#        prev_cols=cols
#        # get terminal size
#        rows=$(tput lines)
#        cols=$(tput cols)
#        if [[ $rows -ne $prev_rows || $cols -ne $prev_cols ]]; then
#          echo "Terminal size changed!"
#          echo "New height: $rows, New width: $cols"
#        # You can add your own logic here to handle the size change
#        fi




        keyname=${keyname#*_}

        case $keyname in
            SPACE)
                if [ $state -eq 1 ]; then
                    xdotool type --clearmodifiers --delay 40 --window $(xdotool getactivewindow) "You are an expert python programmer. "
                fi
                ;;

            LEFTCTRL)
                if [ $state -eq 1 ]; then
                    xdotool type --clearmodifiers --delay 40 --window $(xdotool getactivewindow) "site:news.ycombinator.com"
                fi
                ;;

            LEFTALT)
                if [ $state -eq 1 ]; then
                    xdotool type --clearmodifiers --delay 40 --window $(xdotool getactivewindow) " 1. Guitar tab file server, player, and metronome. 2. AI Agent generation and functioning. 3. Keyboard macros to help me optimize coding productivity. 4. Realtime microphone audio input and analysis, including visualizations and attempts to harmonize output sound with signal. 5. Parsing, segmenting, pattern recognition of music in guitar tab format. 6. Parsing, segmenting and converting to DnD 2e books to DnD 5e. 7. Generating a 20x20 rug hooking pattern from pre-existing photos. 8. Generating a large number of 20x20 rug hooking patterns using generative AI."
                fi
                ;;
            LEFTSHIFT)
                if [ $state -eq 1 ]; then
                    xdotool type --clearmodifiers --delay 40 --window $(xdotool getactivewindow) " Explain this as if you were talking to an 8th grader."
                fi
                ;;


            # UP|DOWN|LEFT|RIGHT)
            #     if [ $state -eq 1 ]; then
            #         py_output=$($HAND_ARROWKEY_SCRIPT $(echo $keyname))
            #     fi
            #     ;;

            *)
                if [ $state -eq 1 ]; then
                  py_output=$($HANDLE_KEY_SCRIPT $(echo $keyname))
                  echo "$py_output"
                fi
                ;;
            # Using tput
        esac




    fi
done
then
    echo "Failed to grab the device. Make sure /dev/input/event# exists and you have the necessary permissions."
    exit 1
fi


# Cleaner Way to do this:
#    case $keyname in
#        KEY_SPACE)
#            py_output=$($HANDLE_KEY_SCRIPT)
#            echo "$py_output"
#            xdotool type --clearmodifiers --delay 40 --window $(xdotool getactivewindow) "You are an expert python programmer. "
#            ;;
#        KEY_KPMINUS)
#            echo "Numpad -"
#            ;;
#        KEY_KPPLUS)
#            echo "++"
#            ;;
#        KEY_KP0)
#            echo "Numpad Zero"
#            ;;
#        KEY_KPDOT)
#            echo "Numpad ."
#            ;;
#        KEY_KPENTER)
#            echo "Numpad Enter"
#            ;;
#        KEY_LEFTCTRL)
#            echo "Ctrl"
#            ;;
#        KEY_ENTER)
#            echo "Regular Enter"
#            ;;
#        KEY_UP|KEY_DOWN|KEY_LEFT|KEY_RIGHT)
#            echo "Keycode: $keyname"
#            ;;
#    esac

