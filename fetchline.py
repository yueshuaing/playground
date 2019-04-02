import os
import xlwt
import re
import sys

if not len(sys.argv) == 2:
	print "#####################"
	print "Please type:"
	print "python fetchline.py path_to_directory"
	print "#####################"
	sys.exit()

book = xlwt.Workbook()
sh = book.add_sheet("sheet_1")

n=0

sh.write(n, 1, "line 2")	
sh.write(n, 2, "line 4")

n+=1

def get_number(input):
	return re.findall(r"[-+]?\d*\.\d+|\d+", input)
	#for each in input.split():
		#if each.isdigit():
			# print each
			#return each

for filename in os.listdir(sys.argv[1]):
    if filename.endswith(".rxt"): 
    	sh.write(n, 0, filename)	

	f=open(filename, "r")

	for i, line in enumerate(f):
		if i == 2: 
			to_be_stored=get_number(line)
			sh.write(n, 1, to_be_stored)
		if i == 5: 
			to_be_stored=get_number(line)
			sh.write(n, 2, to_be_stored)
			n+=1

book.save("output")
