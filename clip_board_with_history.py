import csv
import re
import pyperclip as clip_board

exit_code = 0
previous = ''
my_board = list()
clip_board.copy('')
matcher = re.compile(r'http')
while True:
    content = clip_board.paste()
    if content == 'about:blank':
        break
    if content.startswith('http') and previous != content and content not in my_board:
        my_board.append(content)

        
