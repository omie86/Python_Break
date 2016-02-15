import time
import webbrowser

total_break = 4
break_count = 0
print("Program started on "+time.ctime())
while (break_count < total_break):
    time.sleep(2*60*60)
    webbrowser.open("http://bit.ly/1TiVo40")
    break_count = break_count + 1


