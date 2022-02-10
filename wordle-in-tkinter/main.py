import tkinter as tk
import random

# --- constants ---

WORD_LENGTH = 5

COLOR_GREY   = '#ABABAB'
COLOR_GREEN  = '#9BDB4D'
COLOR_YELLOW = '#FFE16B'

DEBUG = True

# --- functions ---

def debug(*args, **kwargs):
    if DEBUG:
        print('[debug]', *args, **kwargs)
    
def check_word(word):
    return False

def on_click(key):
    global current_row
    global current_col
    global current_word
    
    debug('key:', key)
    
    if key == 'ENTER':
        #if current_col < WORD_LENGTH:
        if len(current_word) < WORD_LENGTH:
            print('too short')
            return
            
        if check_word(current_word):
            for c in range(5):
                all_labels[current_row][c]['bg'] = COLOR_GREY
                char = all_labels[current_row][c]['text']
                all_buttons[char]['bg'] = '#ABABAB'
            # move to next line
            current_row += 1
            current_col = 0
        else:
            pass
            
    elif key == 'BACK':
        if current_col > 0:
            current_col -= 1
            current_word = current_word[:-1]
            all_labels[current_row][current_col]['text'] = ''
    else:
        if current_col < WORD_LENGTH:
            all_labels[current_row][current_col]['text'] = key
            current_col += 1
        else:
            print('too long')

# --- main ---

selected_word = 'banan'.upper()

current_row = 0
current_col = 0
current_word = ''

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

for r in range(1, 1+6):
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
