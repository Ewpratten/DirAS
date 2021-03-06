import sys

debug = False

if len(sys.argv) != 3:
	print("Incorrect usage of command: diras")
	print("	Please use: diras /path/to/file /output/file")
	exit(1)

with open(sys.argv[1]) as File:
	asm_file = [line.split() for line in File]

if debug:
	print("File Loaded")


# create empty list to hold binary instructions
instructions = []
mnemonics = {
	"mov":"10000001",
	"add":"10000010",
	"sub":"10000011",
	"mul":"10000100",
	"div":"10000101",
	"ret":"10000110",
	"call":"10000111",
	"jmpf":"10001000",
	"jmpb":"10001001",
	"jmp":"10001011",
	"paus":"10001100",
	"load":"10001101",
	"rom":"00000011",
	"coredump":"10001110",
	"movs":"10001111",
	"push":"10010000",
	"pop":"10010001",
	"cmp":"10010010",
	"lte":"10010011",
	"gte":"10010100"
}

# Used to convert strings to numbers. A replacement for python's string.ascii_lowercase
string_letters = {
	"_":0,
	"a":1,
	"b":2,
	"c":3,
	"d":4,
	"e":5,
	"f":6,
	"g":7,
	"h":8,
	"i":9,
	"j":10,
	"k":11,
	"l":12,
	"m":13,
	"n":14,
	"o":15,
	"p":16,
	"q":17,
	"r":18,
	"s":19,
	"t":20,
	"u":21,
	"v":22,
	"w":23,
	"x":24,
	"y":25,
	"z":26,
	":":27,
	"1":28,
	".":29,
	"0":30
}

def intError(line_number):
	print("Number larger than 255 found on line:")
	print("	" + str(line_number))
	exit(1)

for line in asm_file:
	
	if len(line) >= 1:
		if not line[0][0] == "#": # If not comment
			
			for mnemonic in line:
				
				# Int
				if mnemonic.isdigit():
					if int(mnemonic) > 255:
						intError(line)
					
					instructions.append('00000001')
					instructions.append(str(format(int(mnemonic), '#010b')[2:]))
				
				# general register
				elif mnemonic[0] == "r" and mnemonic[1:].isdigit():
					if int(mnemonic[1:]) > 255:
						intError(line)
					
					instructions.append('00000010')
					instructions.append(str(format(int(mnemonic[1:]), '#010b')[2:]))
				
				# extended register
				elif mnemonic[0] == "e" and mnemonic[1:].isdigit():
					if int(mnemonic[1:]) > 255:
						intError(line)
					
					instructions.append('00000101')
					instructions.append(str(format(int(mnemonic[1:]), '#010b')[2:]))
				
				# read-only register
				elif mnemonic[0] == "i" and mnemonic[1:].isdigit():
					if int(mnemonic[1:]) > 255:
						intError(line)
					
					instructions.append('00000111')
					instructions.append(str(format(int(mnemonic[1:]), '#010b')[2:]))
				
				# string (strings start with [ )
				elif mnemonic[0] == "[":
					# Turn assembly string into a list [legnth, "text_here"]
					str_explode = [x.strip() for x in mnemonic[1:].split(',')]
					
					# get text from str_explode and strip trailing char "]"
					text = str_explode[1][:int(str_explode[0])]
					
					# Get legnth from str_explode
					legnth = int(str_explode[0])
					
					instructions.append('00000110')
					instructions.append(str(format(int(legnth), '#010b')[2:]))
					
					# Append binary string
					i = 0
					while i < legnth:
						# print(i)
						instructions.append(str(format(int(string_letters[text[i]]), '#010b')[2:]))
						i+=1
				
				# Regular instruction
				else:
					opcode = mnemonics[mnemonic]
					instructions.append(opcode)

if debug:
	print(instructions)

# store assembled code in a file from argv
file = ""
for instruction in instructions:
	file += instruction

f = open(sys.argv[2], "w")
f.write(file)