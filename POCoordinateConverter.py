import struct
import tkinter as tk

# Creates a window for user to input position array
window = tk.Tk()
window.geometry("500x300")
window.title(string="Main Window for Value Input")

# Creates Instructions for viewer in main window.
instructionsLabel = tk.Label(wraplength=500, text="Input your position-array values below, and click the submit button. Each time you click submit, a new window should appear with the results that you can copy. Optionally, you may attatch a name to the values you are converting, so that you don't lose track of which value belongs to what.")
instructionsLabel.pack()

# Instructs viewer to input values in main window
greeting = tk.Label(text="Insert your position-array values.")
greeting.pack()

# Creates entry field for viewer to input values in main window.
entry = tk.Entry(width=500)
entry.pack(padx=10, pady=10)


# Instructs viewer to place optional name for new window.
topWindowNamer = tk.Label(text="(Optional) Give a name/label to your set of values.")
topWindowNamer.pack(padx=10, pady=10)

# Creates optional field for someone to name their windows.
entryNamer = tk.Entry(width=500)
entryNamer.pack(padx=10, pady=10)



name = entry.get()



# Defines this whole thing as a command that can be run?
def VertexOperations():
    # Takes User Input of All Vertex Values
    vertexValues = entry.get()

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

    POHexNo0x = [x.replace("0x", "") for x in POHexConverted]

    # Brings all values into one nice long string
    POHexCleanFinal = ''.join([str(element) for element in POHexNo0x])

    #Creates a new window or area for user to copy the hex code.
    topWindow = tk.Toplevel()
    topWindow.geometry("1000x200")
    windowTitleNamer = entryNamer.get()
    topWindow.title(string=windowTitleNamer)
    optionalName = tk.Label(topWindow, text=windowTitleNamer, font=('Helvetica', 18, 'bold'))
    optionalName.pack()
    resultEntry = tk.Entry(topWindow, width=900)
    resultEntry.insert(0, POHexCleanFinal)
    resultEntry.configure(state="readonly")
    resultEntry.pack(padx=10, pady=10)
    resultCopyLabel = tk.Label(topWindow, text="Copy the hex code above.")
    resultCopyLabel.pack()

# creates button in window
button = tk.Button(window, text="Submit", command=VertexOperations)
button.pack()

# tells the program to wait and listen for things like button presses or something like that idk, and then runs the whole shebang for the program
window.mainloop()
