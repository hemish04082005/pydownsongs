import random
import requests # pip install requests
import bs4 # pip install bs4
import os
import googlesearch # pip install google
import sys
import time

# Random User Agent ------------------
def randomUsrAgent():
	try:
		if not os.path.exists(os.path.join(os.path.expanduser("~"), "randomUsrAgent.txt")):
		    getreq = requests.get("https://raw.githubusercontent.com/tamimibrahim17/List-of-user-agents/master/Chrome.txt")
		    uastrings = getreq.text
		    with open((os.path.join(os.path.expanduser("~"), "randomUsrAgent.txt")), "w")  as file:
		    	file.write("\n".join((uastrings.split("\n")[2:])))
		else:
			uastrings = open("randomUsrAgent.txt", "r").read().split("\n")[2:]
		return random.choice(uastrings)
	except:
		return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
# -------------------------------------

# ping --------------------------------
def ping(url):
	try:
		rand = str(randomUsrAgent())
		usr_agent = {'User-Agent': rand}
		requestget = requests.get(url, headers=usr_agent)
		if requestget.status_code == 200:
			return True
		else:
			return False
	except:
		print("{} not available".format(url))
		return False
# -------------------------------------

def checkInternet(): # Check Internet ------------------
	print("Checking Internet Connection...")
	time.sleep(0.2)
	if ping("https://www.google.com/") == True:
		print("Internet connection is available.")
	else:
		print("It seems that Internet is not available. Please try again.")
		sys.exit()
# ---------------------------------------------------

# Implementation of googlesearch -------
def gSearch(term):
	searchreq = list(googlesearch.search(term, stop=10, num=10, user_agent=(str(randomUsrAgent()))))
	return searchreq
# -------------------------------------