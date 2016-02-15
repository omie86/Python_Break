import time
import webbrowser

i = 0
url = "http://bit.ly/1TiVo40"

print("Program started on "+time.ctime())
while (i < 4):
    time.sleep(7200)
    webbrowser.open(url)
    i = i+1



