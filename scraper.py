import requests
from bs4 import BeautifulSoup
import time
import random
import re

for i in range(499, 0, -1):

	page = requests.get("https://www.oldmasterq.com/comics/" + str(i) + "/")
	soup = BeautifulSoup(page.content, 'html.parser')
	result = soup.find(class_='main-image')

	title = result['alt']
	title = re.sub("[\!\@\#\$\%\^\&\*\(\)\[\]\{\}\;\:\,\.\/\<\>\?\|\`\~\-\=\_]", " ", title)

	path = result['src']

	# Generate random pause
	pause = random.randint(5, 15)
	print("Fetched comic " + str(i) + ", sleeping for " + str(pause) + " seconds.")
	time.sleep(pause)

	image = requests.get("https://www.oldmasterq.com" + path)

	with open("comics/" + str(i) + " - " + title + ".png", "wb") as f:
		f.write(image.content)

	# Generate random pause
	pause = random.randint(7, 13)
	print("Saved comic " + str(i) + ", sleeping for " + str(pause) + " seconds.")
	time.sleep(pause)

print("Done.")