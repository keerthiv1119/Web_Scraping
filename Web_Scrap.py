'''
Author : Keerthi
Id : N151119
Code : Scraping nearly 9000 student images from the college website
'''
import requests
file = open("users.txt","r+")#reading data from files
for line in file:
	k = line.split(':')[0]
	with open(k+'.jpg', 'wb') as handle:
		response = requests.get("http://intranet.rguktn.ac.in/SMS/usrphotos/user/"+str(k)+".jpg", stream=True)
		if not response.ok:
			print(response)
		for block in response.iter_content(1024):
			if not block:
				break
			handle.write(block)
file.close()
