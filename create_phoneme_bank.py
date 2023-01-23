import os
consonants = ["B","CH","D","DH","F","G","HH","JH","K","L","M","N","NG","P","R","S","SH","T","TH", "V","W", "WH", "Y","Z","ZH"]
vowels = ["AA", "AE", "AH", "AO", "AW", "AX", "AXR", "AY", "EH", "ER", "EY", "IH", "IX", "IY", "OW", "OY", "UH", "UW", "UX"]
currdurr = os.getcwd()
parent = consonants + vowels
for i in range(len(parent)):
	os.chdir(currdurr)
	parent_dir = str(parent[i])
	try:
		os.makedirs(parent_dir)
		os.makedirs(parent_dir + "\\" + parent_dir + "0")
		os.makedirs(parent_dir + "\\" + parent_dir + "1")
		os.makedirs(parent_dir + "\\" + parent_dir + "2")
	except FileExistsError:
		pass
	
	