import webbrowser
import os

# Declare your pages here
firstPage = 'https://google.com/'
secondPage = 'https://youtube.com'
thirdPage = 'https://csun.edu'

# Insert the directory of your Chrome application inside ' '
chromeDirectory = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
os.startfile('C:/Program Files/Google/Chrome/Application/chrome.exe', "open")

# Open tabs
webbrowser.get(chromeDirectory).open_new(firstPage)
webbrowser.get(chromeDirectory).open(secondPage)
webbrowser.get(chromeDirectory).open(thirdPage)