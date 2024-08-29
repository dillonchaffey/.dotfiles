#!/bin/bash

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi

readonly MACRO_KBD_NAME="HP USB Keyboard" # bash evtest to get list of plugged in kbds
readonly VENV_SCRIPT_FILEPATH_1="/home/zakalwe/PYCHARM_PROJECTS/my_chat_api_playground/.venv/bin/python /home/zakalwe/PYCHARM_PROJECTS/my_chat_api_playground/main.py"

#IS_RUNNING="false"
#
#while [ "$flag" != "true" ]
#do
#   read x
#   if [ "$x" = "true" ]
#   then
#     flag=true
#   fi
#   echo "${x} : ${flag}"
#done
##'command | pbcopy' and then Ctrl-V elsewhere
#alias pbcopy='xclip -selection clipboard'
#alias pbpaste='xclip -selection clipboard -o'

# Check if evtest is installed
 if ! command -v evtest &> /dev/null; then
     echo "evtest is not installed. Installing now..."
     apt-get update && apt-get install -y evtest
 fi

# Function to convert hex to decimal
hex_to_dec() {
    printf "%d" "0x$1"
}

# Function to check key name

# Function to check key name
is_key_pressed() {
  local key_name="$1"
  local line="$2"
  if [[ $line == *"type 1 (EV_KEY), code $key_name"* ]]; then
    return 0  # Key pressed
  fi
  return 1  # Key not pressed
}

# Function to get key name from code
get_key_name() {
  local code="$1"
  # Replace with your preferred keycode mapping
  case "$code" in
    "0x29") echo "KEY_SPACE" ;;
    # Add more key mappings here
    *) echo "Unknown key" ;;
  esac
}

# Get the event number of the keyboard
keyboard_name=$(grep -Er "$MACRO_KBD_NAME" /sys/class/input/event*/device/name | sort -r)
event_number=$(echo $keyboard_name | cut -d'/' -f5 | cut -d':' -f2)

  if ! evtest --grab "/dev/input/$event_number" | while read -r line; do
    # Extract the key code and state
    code=$(echo $line | awk -F'code ' '{print $2}' | awk '{print $1}' | tr -d ',')
    state=$(echo $line | awk '{print $NF}')

    # Check for key press
    if [ $state -eq 1 ]; then
      key_name=$(get_key_name "$code")
      echo "Key pressed: $key_name"
#
#      # Check for Space key press
#      if is_key_pressed KEY_SPACE "$line"; then
#        IS_RUNNING="true"
#        py_output=$($VENV_SCRIPT_FILEPATH_1)
#        IS_RUNNING="false"
#      fi
    fi
  done
  then
    echo "Failed to grab the device. Make sure /dev/input/event# exists and you have the necessary permissions."
    exit 1
fi

#echo $event_number
#if ! evtest --grab "/dev/input/$event_number" | while read -r line; do
#    if [[ $line == *"type 1 (EV_KEY), code "* ]]; then
#        # Extract the key code and state
#        code=$(echo $line | awk -F'code ' '{print $2}' | awk '{print $1}' | tr -d ',')
#        state=$(echo $line | awk '{print $NF}')
#        dec_code=$(hex_to_dec $code)
##        echo $dec_code
#
#
#        if is_key_pressed KEY_SPACE "$line"; then
#          echo "Space key pressed"
##        # Space
##        if [ $dec_code -eq 87 ] && [ $state -eq 1 ] && [ "$IS_RUNNING" = "false" ]; then #SPACE
##             IS_RUNNING="true"
##             py_output=$($VENV_SCRIPT_FILEPATH_1)
##             IS_RUNNING="false"
#
## read the string with multi line, quotes and no spaces as delimiter
#             agent_output='' read -r -d '' output <<< "$string_with_quotes"
#        # numpad
#        elif [ $dec_code -eq 116 ] && [ $state -eq 1 ]; then #Numpad -
#            echo "Numpad -"
#        elif [ $dec_code -eq 120 ] && [ $state -eq 1 ]; then #Numpad +
#            echo "Numpad +"
#        elif [ $dec_code -eq 130 ] && [ $state -eq 1 ]; then #Numpad 0
#            echo "Numpad Zero"
#        elif [ $dec_code -eq 131 ] && [ $state -eq 1 ]; then #Numpad 0
#            echo "Numpad ."
#        elif [ $dec_code -eq 150 ] && [ $state -eq 1 ]; then #Numpad ENTER
#            echo "Numpad Enter"
#        # Main keys
#        elif [ $dec_code -eq 41 ] && [ $state -eq 1 ]; then #Numpad ENTER
#            echo "Right Ctrl"
#        elif [ $dec_code -eq 40 ] && [ $state -eq 1 ]; then #Numpad ENTER
#            echo "Regular Enter"
#        # Arrows
#        elif [ $dec_code -eq 259 ] && [ $state -eq 1 ]; then #up
#            echo "Keycode: $dec_code"
#        elif [ $dec_code -eq 264 ] && [ $state -eq 1 ]; then #down
#            echo "Keycode: $dec_code"
#        elif [ $dec_code -eq 261 ] && [ $state -eq 1 ]; then #left
#            echo "Keycode: $dec_code"
#        elif [ $dec_code -eq 262 ] && [ $state -eq 1 ]; then #right
#            echo "Keycode: $dec_code"
#        fi
#    fi
#done
#then
#    echo "Failed to grab the device. Make sure /dev/input/event# exists and you have the necessary permissions."
#    exit 1
#fi





# Based on the previously provided image, please finish writing the following code. Include every key and the keys dimensions. use capital letters for the variable names if you are unsure what the key name is.
#
# # Each key is defined by a tuple (x, y, width, height)
# keys = {
#     "esc": (5, 5, 40, 40),
#     "f1": (50, 5, 40, 40),
#     "f2": (95, 5, 40, 40),
#     # Continue defining all keys similarly...
#     "ctrl_right": (1100, 285, 80, 40),
#     "arrow_up": (1055, 245, 40, 40),
#     "arrow_down": (1055, 285, 40, 40),
#     "arrow_left": (1010, 285, 40, 40),
#     "arrow_right": (1100, 285, 40, 40),
#     # Include the rest of the keys in a similar manner...
# }


#
# from PIL import Image
#
# # Load the image
# image_path = './Pasted image 20240812095841.png'
# keyboard_img = Image.open(image_path)
#
# # Example resolution (width, height) of the image
# img_width, img_height = keyboard_img.size
#
# # Data structure for keys
# # Each key is defined by a tuple (x, y, width, height)
# keys = {
#     # First row (top row with Esc and Function keys)
#     "esc": (5, 5, 40, 40),
#     "f1": (60, 5, 40, 40),
#     "f2": (105, 5, 40, 40),
#     "f3": (150, 5, 40, 40),
#     "f4": (195, 5, 40, 40),
#     "f5": (240, 5, 40, 40),
#     "f6": (285, 5, 40, 40),
#     "f7": (330, 5, 40, 40),
#     "f8": (375, 5, 40, 40),
#     "f9": (420, 5, 40, 40),
#     "f10": (465, 5, 40, 40),
#     "f11": (510, 5, 40, 40),
#     "f12": (555, 5, 40, 40),
#     "PRT_SC": (610, 5, 40, 40),
#     "SCR_LK": (655, 5, 40, 40),
#     "PAUSE": (700, 5, 40, 40),
#
#     # Second row (numbers and function keys)
#     "`": (5, 50, 40, 40),
#     "1": (50, 50, 40, 40),
#     "2": (95, 50, 40, 40),
#     "3": (140, 50, 40, 40),
#     "4": (185, 50, 40, 40),
#     "5": (230, 50, 40, 40),
#     "6": (275, 50, 40, 40),
#     "7": (320, 50, 40, 40),
#     "8": (365, 50, 40, 40),
#     "9": (410, 50, 40, 40),
#     "0": (455, 50, 40, 40),
#     "-": (500, 50, 40, 40),
#     "=": (545, 50, 40, 40),
#     "backspace": (600, 50, 90, 40),
#
#     # Third row (Tab and QWERTY)
#     "tab": (5, 95, 60, 40),
#     "q": (70, 95, 40, 40),
#     "w": (115, 95, 40, 40),
#     "e": (160, 95, 40, 40),
#     "r": (205, 95, 40, 40),
#     "t": (250, 95, 40, 40),
#     "y": (295, 95, 40, 40),
#     "u": (340, 95, 40, 40),
#     "i": (385, 95, 40, 40),
#     "o": (430, 95, 40, 40),
#     "p": (475, 95, 40, 40),
#     "[": (520, 95, 40, 40),
#     "]": (565, 95, 40, 40),
#     "\\": (610, 95, 80, 40),
#
#     # Fourth row (Caps Lock and ASDF row)
#     "caps_lock": (5, 140, 75, 40),
#     "a": (85, 140, 40, 40),
#     "s": (130, 140, 40, 40),
#     "d": (175, 140, 40, 40),
#     "f": (220, 140, 40, 40),
#     "g": (265, 140, 40, 40),
#     "h": (310, 140, 40, 40),
#     "j": (355, 140, 40, 40),
#     "k": (400, 140, 40, 40),
#     "l": (445, 140, 40, 40),
#     ";": (490, 140, 40, 40),
#     "'": (535, 140, 40, 40),
#     "enter": (580, 140, 110, 40),
#
#     # Fifth row (Shift and ZXCV row)
#     "shift_left": (5, 185, 100, 40),
#     "z": (110, 185, 40, 40),
#     "x": (155, 185, 40, 40),
#     "c": (200, 185, 40, 40),
#     "v": (245, 185, 40, 40),
#     "b": (290, 185, 40, 40),
#     "n": (335, 185, 40, 40),
#     "m": (380, 185, 40, 40),
#     ",": (425, 185, 40, 40),
#     ".": (470, 185, 40, 40),
#     "/": (515, 185, 40, 40),
#     "shift_right": (560, 185, 130, 40),
#
#     # Sixth row (Control and Spacebar row)
#     "ctrl_left": (5, 230, 60, 40),
#     "fn": (70, 230, 50, 40),
#     "windows": (125, 230, 50, 40),
#     "alt_left": (180, 230, 60, 40),
#     "space": (245, 230, 275, 40),
#     "alt_right": (525, 230, 60, 40),
#     "CTRL": (590, 230, 100, 40),
#
#     # Navigation keys
#     "INSERT": (720, 50, 50, 40),
#     "HOME": (775, 50, 50, 40),
#     "PG_UP": (830, 50, 50, 40),
#     "DELETE": (720, 95, 50, 40),
#     "END": (775, 95, 50, 40),
#     "PG_DN": (830, 95, 50, 40),
#     "arrow_up": (780, 185, 50, 40),
#     "arrow_left": (725, 230, 50, 40),
#     "arrow_down": (780, 230, 50, 40),
#     "arrow_right": (835, 230, 50, 40),
#
#     # Numeric keypad
#     "num_lock": (900, 50, 50, 40),
#     "divide": (955, 50, 50, 40),
#     "multiply": (1010, 50, 50, 40),
#     "subtract": (1065, 50, 50, 40),
#     "7": (900, 95, 50, 40),
#     "8": (955, 95, 50, 40),
#     "9": (1010, 95, 50, 40),
#     "add": (1065, 95, 50, 90),
#     "4": (900, 140, 50, 40),
#     "5": (955, 140, 50, 40),
#     "6": (1010, 140, 50, 40),
#     "1": (900, 185, 50, 40),
#     "2": (955, 185, 50, 40),
#     "3": (1010, 185, 50, 40),
#     "enter": (1065, 185, 50, 90),
#     "0": (900, 230, 105, 40),
#     "decimal": (1010, 230, 50, 40)
# }
#
#
# # Function to calculate the surface area of a key
# def key_area(key):
#     _, _, width, height = keys[key]
#     return width * height
#
# # Sort keys by area
# sorted_keys = sorted(keys.keys(), key=key_area, reverse=True)
#
# # Initialize four groups
# groups = {1: [], 2: [], 3: [], 4: []}
# group_areas = {1: 0, 2: 0, 3: 0, 4: 0}
#
# # Distribute keys among groups
# for key in sorted_keys:
#     smallest_group = min(group_areas, key=group_areas.get)
#     groups[smallest_group].append(key)
#     group_areas[smallest_group] += key_area(key)
#
# # Display the groups and their total surface areas
# for i in range(1, 5):
#     print(f"Group {i}:")
#     for key in groups[i]:
#         print(f"  {key}: area = {key_area(key)}")
#     print(f"Total area: {group_areas[i]}\n")








    Mastery = (
        "novice", "apprentice", "journeyman", "expert", "specialist", "master",
        "grandmaster", "trailblazer", "visionary", "legend"
    )
    Style = (
        "imperative", "functional", "object_oriented", "procedural", "declarative",
        "event_driven", "logic", "aspect_oriented", "domain_specific_language", "metaprogramming"
    )
    Focus = (
        "data_structures", "design_patterns", "software_architecture", "testing",
        "debugging", "security", "performance", "documentation"
    )
    Domain = (
        "finance", "healthcare", "e_commerce", "education", "manufacturing",
        "transportation", "telecommuncations", "gaming", "social_media",
        "music",
    )
    Communication = (
        "active_listening", "clarity", "diplomacy", "empathy", "persuasion",
        "presentation", "writing", "conflict_resolution", "cultural_awareness", "feedback"
    )
    ProblemSolving = (
        "data_driven", "algorithmic", "heuristic", "model_based", "design_thinking",
        "root_cause_analysis", "systematic", "collaborative", "agile", "creative", "experimental"
    )
    Testing



# Define PersonaTypes based on the provided attributes
PersonaTypes = {
    "Mastery": (
        "novice", "apprentice", "journeyman", "expert", "specialist", "master",
        "grandmaster", "trailblazer", "visionary", "legend"
    ),
    "Style": (
        "imperative", "functional", "object_oriented", "procedural", "declarative",
        "event_driven", "logic", "aspect_oriented", "domain_specific_language", "metaprogramming"
    ),
    "Focus": (
        "data_structures", "design_patterns", "software_architecture", "testing",
        "debugging", "security", "performance", "documentation", "writing_working_code",
        "writing_better_code", "writing_clean_code", "writing_elegant_code",
        "writing_fast_code", "writing_optimized_code", "writing_reusable_code",
        "linux", "geospatial", "remote_sensing", "image_processing", "data_science"
    ),
    "Domain": (
        "finance", "healthcare", "e_commerce", "education", "manufacturing",
        "transportation", "telecommunications", "gaming", "social_media",
        "music", "social_networking", "blockchain", "cloud_computing",
        "virtual_reality", "augmented_reality", "virtual_worlds", "3d_graphics",
        "game_development", "web_development", "mobile_development", "drones",
        "geographic_science", "artificial_intelligence", "backend_development",
        "command_line_applications", "full_stack_development"
    ),
    "Communication": (
        "active_listening", "clarity", "diplomacy", "empathy", "persuasion",
        "presentation", "writing", "conflict_resolution", "cultural_awareness", "feedback"
    ),
    "ProblemSolving": (
        "data_driven", "algorithmic", "heuristic", "model_based", "design_thinking",
        "root_cause_analysis", "systematic", "collaborative", "agile", "creative", "experimental"
    ),
    "Testing": (
        "unit_testing", "integration", "acceptance_testing", "regression",
        "performance", "security", "usability", "exploratory", "continuous", "risk_based"
    ),
}
persona_data = {
    'low_level_dev': {
        'Mastery': 'grandmaster',
        'Style': 'imperative',
        'Focus': 'data_structures',
        'Domain': 'backend_development',
        'Communication': 'clarity',
        'ProblemSolving': 'data_driven',
        'Testing': 'unit_testing'
    },
    'python_terminal_dev': {
        'Mastery': 'legend',
        'Style': 'functional',
        'Focus': 'design_patterns',
        'Domain': 'command_line_applications',
        'Communication': 'clarity',
        'ProblemSolving': 'algorithmic',
        'Testing': 'integration'
    },
    'quality_assurance': {
        'Mastery': 'master',
        'Style': 'object_oriented',
        'Focus': 'software_architecture',
        'Domain': 'full_stack_development',
        'Communication': 'diplomacy',
        'ProblemSolving': 'heuristic',
        'Testing': 'acceptance_testing'
    },
    'project_manager': {
        'Mastery': 'visionary',
        'Style': 'procedural',
        'Focus': 'testing',
        'Domain': 'education',
        'Communication': 'empathy',
        'ProblemSolving': 'model_based',
        'Testing': 'regression'
    }
}




#!~/PYCHARM_PROJECTS/my_chat_api_playground/.venv/bin/python
# personalities for AI agents
# example usage: custom personality
# new_persona = persona_type_defaults['low_level_dev'].copy()
# new_persona['Name'] = 'John Doe'

# another custom #NEW
# bot = ProgrammerBot()
# bot = set_persona(bot, 'low_level_dev', {'Mastery': 'ninja'})

class PersonaTypes:
    Mastery = {
        "novice", "apprentice", "journeyman", "expert", "specialist", "master",
        "grandmaster", "trailblazer", "visionary", "legend"
    }
    Style = {
        "imperative", "functional", "object_oriented", "procedural", "declarative",
        "event_driven", "logic", "aspect_oriented", "domain_specific_language", "metaprogramming"
    }
    Focus = {
        "data_structures", "design_patterns", "software_architecture", "testing",
        "debugging", "security", "performance", "documentation", "writing_working_code",
    }
    Domain = {
        "finance", "healthcare", "e_commerce", "education", "manufacturing",
        "transportation", "telecommuncations", "gaming", "social_media",
    }
    Communication = {
        "active_listening", "clarity", "diplomacy", "empathy", "persuasion",
        "presentation", "writing", "conflict_resolution", "cultural_awareness", "feedback"
    }
    ProblemSolving = {
        "data_driven", "algorithmic", "heuristic", "model_based", "design_thinking",
        "root_cause_analysis", "systematic", "collaborative", "agile", "creative", "experimental"
    }
    Testing = {
        "unit_testing", "integration", "acceptance_testing", "regression",
        "performance", "security", "usability", "exploratory", "continuous", "risk_based"
    }

persona_type_defaults = {
    'low_level_dev': {
        'Mastery': 'grandmaster',
        'Style': 'imperative',
        'Focus': 'data_structures',
        'Domain': 'backend_development',
        'Communication': 'clarity',
        'ProblemSolving': 'data_driven',
        'Testing': 'unit_testing'
    }
}





class ProgrammerBot:
    def __init__(self):
        self.state = {
            "Mastery": set(),
            "Style": set(),
            "Focus": set(),
            "Domain": set(),
            "Communication": set(),
            "ProblemSolving": set(),
            "Testing": set()
        }

import random


def set_persona(bot, persona_type, kwargs):
  if persona_type not in persona_type_defaults:
    raise ValueError(f"Invalid persona type: {persona_type}")

  # Apply the persona type defaults
  for attribute, value in persona_type_defaults[persona_type].items():
    bot.state[attribute] = value

  # Override with custom attributes
  for attribute, value in kwargs.items():
    bot.state[attribute] = value

  return bot



if __name__ == "__main__":
  bot = ProgrammerBot()
  bot = set_personality_randomly(bot)
  print(bot.state.keys(), bot.state.values())



  print ('ending("persona.py")')





















with open(os.path.join('./TMP', f'{botname}_OUTPUT.TXT'), 'w') as f:
    f.write(code_inside)








