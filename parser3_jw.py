import argparse
parser = argparse.ArgumentParser()
parser.add_argument("row_type", help = "which rows of data to extract, i.e. 'ATT' ")
parser.add_argument("attribute_type", help = "what attributes to extract, i.e. 'raw' ")
parser.add_argument("--outputfile", help = "optional output file, values will be printed to terminal if not specified")
args = parser.parse_args()

# input_dict should be from the other file, here is just for testing
input_dict = {"ATT":["raw", "pitch", "yaw"]}

l = len(input_dict[args.row_type])
dict = {}  # output dictionary
# initialize the dictionary
for item in input_dict[args.row_type]:
	dict[item] = []


log = open('samplelog.log','r')
if (args.outputfile):
	output = open(args.outputfile,'w')

# read each line with specific attribute then read into the dictionary
for line in log.readlines():
	arr = line.split(',')
	if (arr[0]== args.row_type):
		for i in range(0, l):
			dict[input_dict[args.row_type][i]].append((float)(arr[i+2].strip()))

log.close()

for i in dict[args.attribute_type]:
	if (args.outputfile):
		output.write(str(i)+'\n')
	else:
		print(i)

if (args.outputfile):
	output.close()