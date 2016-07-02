import wget
import os
import json
import sys
import urllib.request
import urllib
from urllib.request import urlopen
from subprocess import check_output

link = "http://localhost/"

if len(sys.argv) <= 1 or len(sys.argv) >= 5:
	print("Usage: python3 cyberApi <upload/download> <cyberstick id>")
	quit()
else:
	if sys.argv[1] == "download":
		text = urlopen(link+"api/download/"+sys.argv[2]).read().decode('utf-8')
		filej = json.loads(text)["zfile"]
		seis = json.loads(text)["xfile"]
		for zfile in filej:
			print("Downloading "+zfile['name']+" of type "+zfile['extension']+"..")
			file_url = link + "static/uploads/" + seis['session'] + "/" + zfile['name'] + '.' + zfile['extension']
			file_name = wget.download(file_url)
	if sys.argv[1] == "upload":
		fileLink = '"file=@'+sys.argv[2]+'"'
		command = "curl -F "+fileLink+" "+link+"api/upload"
		upload_call = os.popen(command).read()
		print(upload_call)
		print("\n")
