# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2022.02.10

import tkinter as tk
import random

# --- constants ---

WORD_LENGTH = 5
MAX_WORDS = 6

COLOR_GREY   = '#ABABAB'
COLOR_GREEN  = '#9BDB4D'
COLOR_YELLOW = '#FFE16B'

DEBUG = True

# --- functions ---

def debug(*args, **kwargs):
    if DEBUG:
        print('[debug]', *args, **kwargs)
    
def check_word(word):
    result = []
    status = True
    debug('[check_word] word:', word)
    for n, char in enumerate(word):
        debug('[check_word] ', n, char, selected_word[n])
        if char == selected_word[n]:
            result.append(COLOR_GREEN)
        elif char in selected_word:
            result.append(COLOR_YELLOW)
            status = False
        else:
            result.append(COLOR_GREY)
            status = False
        
    return status, result

def reset():
    global selected_word
    global current_row
    global current_col
    global current_word

    selected_word = random.choice(words).upper()

    current_row = 0
    current_col = 0
    current_word = ''

    for key in all_buttons.values():
        key['bg'] = None

    for word_labels in all_labels:
        for label in word_labels:
            label['text'] = ''
            label['bg'] = 'white'
        
def on_click(key):
    global current_row
    global current_col
    global current_word
    
    debug('[on_click] key:', key)

    label_message['text'] = ''

    if current_row >= MAX_WORDS:
        label_message['text'] = 'Press ENTER to start'
        
        return
    
    if key == 'ENTER':
        if current_row >= MAX_WORDS:
            reset()
            return
        
        #if current_col < WORD_LENGTH:
        if len(current_word) < WORD_LENGTH:
            label_message['text'] = 'too short'
            return
            
        status, result = check_word(current_word)
        debug('[on_click]:', status, result)
        
        for c, (char, color) in enumerate(zip(current_word, result)):
            all_labels[current_row][c]['bg'] = color
            char = all_labels[current_row][c]['text']
            if all_buttons[char]['bg'] != COLOR_GREEN:
                all_buttons[char]['bg'] = color
                
        if not status:
            # move to next line
            current_row += 1
            current_col = 0
            current_word = ''
        else:
            pass
        
        if current_row >= MAX_WORDS:
            label_message['text'] = f'correct: {selected_word}'
            
    elif key == 'BACK':
        if current_col > 0:
            current_word = current_word[:-1]
            current_col -= 1
            all_labels[current_row][current_col]['text'] = ''
    else:
        if current_col < WORD_LENGTH:
            current_word += key
            all_labels[current_row][current_col]['text'] = key
            current_col += 1
        else:
            label_message['text'] = 'too long'

# --- main ---

words = ['banan', 'canon', 'kajak']

# - (re)set data -

selected_word = random.choice(words).upper()

current_row = 0
current_col = 0
current_word = ''

#reset()

# -  -

root = tk.Tk()
root.title('PyWORDLE')
root.resizable(False, False)

default_color = root['bg']
debug('bg:', default_color)

# - GUI words -

frame_words = tk.Frame(root)
frame_words.pack()

all_labels = []

for r in range(MAX_WORDS):
    word_labels = []
    all_labels.append(word_labels)
    for c in range(WORD_LENGTH):
        label = tk.Label(frame_words,
                         #text='',
                         relief='solid',
                         bg='white',
                         pady=8,
                         width=3,
                         font=(None, 16, 'bold'))
        label.grid(row=r, column=c, padx=3, pady=3)
        word_labels.append(label)

# - GUI message -

label_message = tk.Label(root, pady=8, font=(None, 16, 'bold'))
label_message.pack()
        
# - GUI keyboard -

keyboard = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['ENTER', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'BACK'],
    ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ż', 'ź'],
]

all_buttons = {}

for line in keyboard:
    frame_keyboard_line = tk.Frame(root)
    frame_keyboard_line.pack()
    for c, key in enumerate(line):
        key = key.upper()
        cmd = lambda text=key:on_click(text)
        button = tk.Button(frame_keyboard_line, text=key, command=cmd)
        button.grid(row=0, column=c)
        all_buttons[key] = button
        
# - start -

root.mainloop()
