# DirAS
The Dirobium ASsembler (pronounced dir-as)

## Installation
Make sure you have python3 installed before following these steps.

First, clone this repo to a safe place (like your home directory). Then run this in your terminal:
```bash
echo "#\!/bin/bash" > /usr/local/bin/diras
echo "python3 </path/to/diras/repo>/src $1 $2" >> /usr/local/bin/diras
chmod 755 /usr/local/bin/diras
```

You should now be able to type `diras` into your terminal, and see this:
```
Incorrect usage of command: diras
        Please use: diras /path/to/file /output/file
```

## Mnemonics
DirAS' mnemonics map directly to the Dirobium basic instruction set. They are:

| mnemonic | example     | description                                                                         |
|----------|-------------|-------------------------------------------------------------------------------------|
| mov      | mov 1 r1    | moves a value to a loaction                                                         |
| add      | add 1 5 r2  | adds two values and stores them in a location                                       |
| sub      | sub 7 18 r3 | subtracts two values and stores them in a location                                  |
| mull     | mull 8 8 r4 | multiplies two values and stores them in a location                                 |
| div      | div 6 12    | divides two values and stores them in a location                                    |
| ret      | ret 1       | stores a value in the return register (e1)                                          |
| call     | call 1      | calls a device or function with the corresponding id                                |
| load     | load rom    | loads something into memory                                                         |
| jmp      | jmp rom 0   | jumps to a function or file loaded into memory at specified location (if supported) |
| jmpf     | jmpf 20     | jumps forward 20 instructions (not yet supported)                                   |
| jmpb     | jmpb 40     | jumps backwards 40 instructions (not yet supported)                                 |

## Registers
The registers: r0 - r9 can be used for whatever you would like.
The registers: e0 - e9 are used for calling functions and other system calls.
The register: e1 is for storing a return value. Do not edit directly, use the `ret` mnemonic.

## Building a program
To build a program for the Dirobium emulator, use:
```
diras /path/to/input/file ./main.rom
```

Then copy `main.rom` into the root of your Dirobium emulation environment.

(main program is called `main.rom` and the bootloader is called `bootloader.rom` do not mix these up)
