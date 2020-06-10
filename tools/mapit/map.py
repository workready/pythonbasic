import webbrowser
import sys
import pyperclip


if len(sys.argv) > 1:
    address = sys.argv[1]
else:
    address = pyperclip.paste()

webbrowser.open(f'https://www.google.com/maps/place/{address}')