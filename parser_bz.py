# Filename: parser_bz.py
# Author: Lichen (Brittany) Zhang
# Date: Jan 22 2017
# Description: 
#     This program reads a log file, extracts lines that starts with
#     certain characters, and print these lines into output.txt.
# Sources of help: 
#     Youtube video https://www.youtube.com/watch?v=1uA-pLITer0 
#     parser_jw.py by Jiayin (Jenny) Wang

def main():
   
   # read file
   # can pass an object instead of specific file name here
   file = open( "samplelog.log", "r" )  
   lines = file.readlines()
   file.close()

   # look for patterns
   countATT = 0
   out = open( 'out.txt', 'w' )
   
   for line in lines:
      array = line.split(',')

      if (array[0] == "ATT"):
         print >> out, line
         countATT = countATT + 1

   out.close()
   # display result
   print "Found", countATT, "lines that start with 'ATT'."

main()




