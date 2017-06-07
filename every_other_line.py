import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", help = "original file")
parser.add_argument("outputfile", help = "output file")
args = parser.parse_args()

input = open(args.file, 'r')
output = open(args.outputfile, 'w')
i = 1
for line in input.readlines():
	if (i%2 == 1):
		output.write(line)
	i = i + 1

input.close()
output.close()
