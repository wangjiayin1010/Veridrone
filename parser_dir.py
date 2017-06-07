import numpy as np
import cmath
import argparse
import fileinput
import csv


from itertools import zip_longest

# Nathan's algorithm to calculate angles
# So far this should be correct for small angles
def rpy2dir(roll, pitch, yaw):
    # type: (object, object, object) -> object
    c1 = np.cos(yaw);
    c2 = np.cos(pitch);
    c3 = np.cos(roll);
    s1 = np.sin(yaw);
    s2 = np.sin(pitch);
    s3 = np.sin(roll);

    Rx = np.array([[1, 0, 0],
                   [0, c(roll), -s(roll)],
                   [0, s(roll), c(roll)]])
    Ry = np.array([[c(pitch), 0, s(pitch)],
                   [0, 1, 0],
                   [-s(pitch), 0, c(pitch)]])
    Rz = np.array([[c(yaw), -s(yaw), 0],
                   [s(yaw), c(yaw), 0],
                   [0, 0, 1]])
    Rot = np.dot(Rz, Ry)
    Rot = np.dot(Rot, Rx)
    # print(Rx)
    # print(Ry)
    # print(Rz)
    # print(Rot)
    up = np.array([[0], [0], [-1]])
    updir = np.dot(Rot, up)
    # print(updir)
    return np.rad2deg(np.arctan2(updir[1], updir[0]))[0]


def c(theta):
    return np.cos(np.deg2rad(theta))


def s(theta):
    return np.sin(np.deg2rad(theta))

parser = argparse.ArgumentParser()
parser.add_argument("roll", help = "file containing rolls")
parser.add_argument("pitch", help = "file containing pitch")
parser.add_argument("yaw", help = "file containing yaw")
parser.add_argument("gcrs", help = "file containint gcrs")
parser.add_argument("output", help = "csv file with 7 columns")
args = parser.parse_args()

# Read each line from raw, pitch and yaw (using loop)
print ('Reading each line from raw, pitch and yaw...')

with open(args.roll, 'r') as file1, open(args.pitch, 'r') as file2, open(args.yaw, 'r') as file3, \
        open(args.gcrs, 'r') as file4, open(args.output, 'w') as csv_file:
    for x, y, z, a in zip(file1, file2, file3, file4):
        # x for roll, y for pitch, z for yaw
        # a for gcrs
        x = (float)(x.strip());
        y = (float)(y.strip());
        z = (float)(z.strip());
        a = (float)(a.strip());

        # print to see if values are correct
        #print("{0}, {1}, {2}".format(x, y, z))

        # now write to a csv file

        # 1st column: label (0 if no wind; 1 if there is wind)
        csv_file.write((str)(0))
        csv_file.write(",")

        # 2nd column: roll
        csv_file.write((str)(x))
        csv_file.write(",")

        # 3rd column: pitch
        csv_file.write((str)(y))
        csv_file.write(",")

        # 4th column: yaw
        csv_file.write((str)(z))
        csv_file.write(",")

        # 5th column: angle
        w = (rpy2dir(x, y, z))
        csv_file.write((str)(w))
        csv_file.write(",")

        # 6th column: GCRS (Ground course in degrees (0 = north))
        csv_file.write((str)(a))
        csv_file.write(",")

        # 7th column: The difference between GCRS value and the angle in column 5
        # csv_file.write((str)(a-w))
        csv_file.write((str)(min(abs(a-w), abs(a-w-360))))

        csv_file.write("\n")




csv_file.close()
file1.close()
file2.close()
file3.close()


