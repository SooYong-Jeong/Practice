'''
f = open("test_csv.csv", "a")
line = "a1, a01, a02, a03\n"
f.write(line)
line = "b1, b01, b02, b03\n"
f.write(line)
line = "c1, c01, c02, c03\n"
f.write(line)
f.close()

f = open("test_csv.csv", "r")
lines = f.readlines()
print(lines)
f.close()
'''
import csv

f=open("test_csv.csv", "r")

lines=csv.reader(f)
header = next(lines)
for line in lines:
    print(line)

f.close()