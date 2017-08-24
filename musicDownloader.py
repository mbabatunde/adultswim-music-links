#!/usr/bin/env python3
__author__ == "Mark Babatunde"

import urllib.request
import json

def adultSwim():
	with urllib.request.urlopen("https://singles2017.s3.amazonaws.com/data/data.json") as url:
		data = json.loads(url.read().decode())
		for item in data["singles"]:
			print (item["title"] + ":" + "\t" + item["artist_name"] + "\t" + item["mp3_file"])
if __name__ == "__main__":
	adultSwim()

