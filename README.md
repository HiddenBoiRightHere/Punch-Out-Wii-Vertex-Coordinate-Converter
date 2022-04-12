# Punch-Out-Wii-Vertex-Coordinate-Converter
This Python 3 program is designed to take the numbers from position arrays that a user copy-pastes and organize them into the same format that Punch-Out!! Wii uses within it's own hex code.

This doesn't particularly mean that Punch-Out!! Wii is the only system that may benefit from this program, all it does is take some numbers, reorganize them, and turn them into hex code. Quite frankly, this has been more of a project for me to start learning Python and begin to understand how to use StackOverflow to help solve my problems in a jam haha! 

# Some Important Notes
The conversions **only** work when your numbers in groups of three. Examples:

Input: 1
---

Output: Nothing


Input: 1 2 3 4
---

Output: Hex conversion for 1, -3, 2.

Input: 1 2 3
---

Output: Hex conversion for 1, -3, 2.

Please also note that these conversions are only one-way. You cannot convert hex to numbers using this program.

# How it works
It's rather simple. You take a set of vertex coordinates, which are always in groups of 3, copy them and run the program. The program will ask for a user's input, they paste in the numbers, and it begins. The numbers the user has put in get split into three lists of X, Y, and Z coordinates. Then these are converted to float-numbers. Then the Z-coordinate floats become negative, and then the lists are re-interleaved in the order of X, -Z, Y. Lastly, they are all put into one big list, converted to hex code, converted into a string, and then all of the 0x gets removed to create one long string of hex code that users can place into a hex file. Tada! It sure took me a while to figure out, but it was fun. 

I look forward to trying to make more!

-HiddenBoi
