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
	"coredump":"10001110"
}

for line in asm_file:
	if len(line) >= 1:
		if not line[0][0] == "#":
			for mnemonic in line:
				if mnemonic.isdigit():
					if int(mnemonic) > 255:
						print("Found int larger than 256 in line:")
						print(line)
						exit(1)
					instructions.append('00000001')
					instructions.append(str(format(int(mnemonic), '#010b')[2:]))
				elif mnemonic[0] == "r" and mnemonic[1:].isdigit():
					if int(mnemonic[1:]) > 255:
						print("Found int larger than 256 in line:")
						print(line)
						exit(1)
					instructions.append('00000010')
					instructions.append(str(format(int(mnemonic[1:]), '#010b')[2:]))
				elif mnemonic[0] == "e" and mnemonic[1:].isdigit():
					if int(mnemonic[1:]) > 255:
						print("Found int larger than 256 in line:")
						print(line)
						exit(1)
					instructions.append('00000101')
					instructions.append(str(format(int(mnemonic[1:]), '#010b')[2:]))
				else:
					opcode = mnemonics[mnemonic]
					instructions.append(opcode)

if debug:
	print(instructions)

# print out assembled bin for pipe into file
file = ""
for instruction in instructions:
	file += instruction

f = open(sys.argv[2], "w")
f.write(file)