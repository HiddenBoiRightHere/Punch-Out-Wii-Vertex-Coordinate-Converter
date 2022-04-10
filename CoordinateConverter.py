import struct

# Takes User Input of All Vertex Values
vertexValues = input("Enter your value:  ")

# Splits all Vertex Values into list values
vertexXSplit = vertexValues.split()

# Splits vertexXSplit into x, y, and z in order.
xOriginal = vertexXSplit[::3]
yOriginal = vertexXSplit[1::3]
zOriginal = vertexXSplit[2::3]

# Conversions, AKA Converting the lists to actual numbers for math
XNumberList = [float(xOriginal) for xOriginal in xOriginal]
YNumberList = [float(yOriginal) for yOriginal in yOriginal]
ZNumberList = [float(zOriginal) for zOriginal in zOriginal]

# Convert negative to positive and positive to negative in the ZNumberList list. (Converts z to -z.)
ZNumberList = [-1 * ZNumberList for ZNumberList in ZNumberList]

# Reorders the Number list to (x, -z, y) and combines them into one list.
lists = [XNumberList, ZNumberList, YNumberList]
POFinal = [val for tup in zip(*lists) for val in tup]

# Converting values to hex.

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])

i = 0
POHexConverted = []
while i < len(POFinal):
    POHexAppender = float_to_hex(POFinal[i])
    POHexConverted.append(POHexAppender)
    i = i + 1

# Removes 0x in front of coordinates.

POHexNo0x = [x.replace("0x","") for x in POHexConverted]

# Prints values as a test
POHexCleanFinal = ''.join([str(element) for element in POHexNo0x])
print(POHexCleanFinal)


