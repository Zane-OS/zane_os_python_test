#! python3 /user/bin/env python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard
"""
这个 python 主要功能，将从剪贴板取得文本，并在每一行的开始加上*号
1、从剪贴板粘贴文本
2、对它做处理
3、将新的文本复制到剪贴板
"""

import pyperclip
text = pyperclip.paste()
# TODO: Separate lines and add stars

lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes in the 'lines' list
    lines[i] = '* '+lines[i] # add star to each string in 'lines' list
text = '\n'.join(lines)
pyperclip.copy(text)