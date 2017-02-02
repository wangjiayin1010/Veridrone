import csv
import sys

def main():

   print "This algorithm should parse a log file."

   #print out only the lines that contain a certain string

   infile = open("log.txt", "r");
   outfile = open("output.txt", "w");
   
   lines = infile.readlines()
   countLines = 0;

   print ( "Printing FMT lines into output.txt" )
   for line in lines:
       if "FMT" in line:
         outfile.write(line)


   infile.close()
   outfile.close()

   #print out everything:

   #iofile = open("log.txt", "r");
   #liners = iofile.readlines()
   #countLiners = 0;

   #for x in range(0, 3):
      #print ("Printing x in range" )
      #print ( liners )
      #print ( "\n" )
      
   #iofile.close()

main()
