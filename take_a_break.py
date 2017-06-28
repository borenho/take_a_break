import time
import webbrowser

print ("This program started on " + time.ctime())
for i in range(3):  # Do this 3 times
	time.sleep(2*60*60)  # time.sleep takes time in sec, my arg takes 2 hrs
	webbrowser.open("http://www.ustream.tv/channel/jesusislord-radio")
