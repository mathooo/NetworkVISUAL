import sys
import fileinput

python_file = sys.argv[-2]
path = sys.argv[-1]

with open(python_file, 'r') as file :
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('/home/matho/node_modules/vis/dist/', path)

# Write the file out again
with open(python_file, 'w') as file:
    file.write(filedata)