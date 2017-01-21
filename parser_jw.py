import argparse
parser = argparse.ArgumentParser()
parser.add_argument("row_type", help = "which rows of data to extract, i.e. 'ATT' ")
parser.add_argument("attribute_type", help = "what attributes to extract, i.e. 'raw' ")
parser.add_argument("--outputfile", help = "optional output file, values will be printed to terminal if not specified")
args = parser.parse_args()

dict = {'raw':[],
        'pitch':[],
        'yaw':[]}
log = open('samplelog.log','r')
if (args.outputfile):
	output = open(args.outputfile,'w')

for line in log.readlines():
	arr = line.split(',')
	if (arr[0]== args.row_type):
		dict["raw"].append((float)(arr[3].strip()))
		dict["pitch"].append((float)(arr[4].strip()))
		dict["yaw"].append((float)(arr[5].strip()))
log.close()

for i in dict[args.attribute_type]:
	if (args.outputfile):
		output.write(str(i)+'\n')
	else:
		print(i)

if (args.outputfile):
	output.close()

