# Veridrone

Most files for up and down prediction are in updownPredict directory. Data in raining.csv and testing.csv are acquired from samplelog.log, then parsed and split into training data and testing data. The columns are: 
TimeUs; altitude; delta of altitude; label; TimeUs; z axis acceleration; TimeUs; motor1 thrust; motor2 thrust; motor3 thrust; motor4 thrust; average thrust; delta in average thrust; TimeUs; thrust in;

Classification.py and classification(only motor).py are classifiers for predicting up and down of the quadcopter. Columns of features can be changed through the index numbers. 

All the logs: Log 17 - Flying N with no wind; 
Log 19, 14, 15, 16 - All flights flown with wind at 2 m/s and altitude at 40m, each quadcopter reached a velocity of approx 4-5 m/s in their flights, Log 19 flown N, Log 14 flown E, Log 15 flown S, Log 16 flown W; 
Log 21, 22, 23, 24 - Flight logs in diagonal directions, all flights flown with wind at 2 m/s in dir. of 180 degrees, and altitude at 40m, Log 21 flown NE, Log 22 flown SE, Log 23 flown SW, Log 24 flown NW;

Most files about windy prediction are on Brittany_parser_nowind branch. There’s parseLog_notes.txt that has documentation on how the parsers in this directory work. The classifier is on master branch windy directory. The ml_training.csv and ml_testing.csv are processed data from multiply flights. 

In the log directory, all files ending with .log are raw data. Files ending with _result.log are processed data used for windy classification, the columns are theoretical orientation (calculated from roll, pitch, yaw), actual orientation (read from gcrs from GPS), their value difference, and label (1 for windy and 0 for non-windy). These results files are just for reference. If you do it with the parsers above the result files would be slightly different but do the same thing.
