#! /bin/python3
# Program to convert a list of given numbers to ducky script

import sys

initial_delay		= 2000
command_delay		= 500
protection_delay	= 30200
guess				= 0

if len(sys.argv) < 3 or len(sys.argv) > 3:
	print("Usage: ./programname passwordfile outputfile")
	sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
	with open(input_file, 'r') as source_file:
		with open(output_file, 'w') as target_file:
			target_file.write("DELAY ")
			target_file.write(str(initial_delay))
			target_file.write("\n")
			for line in source_file:
				target_file.write("STRING " + line)
				target_file.write("DELAY 100\n")
				target_file.write("ENTER\n")
				if guess < 10:
					target_file.write("DELAY " + str(command_delay) + "\n")
				guess += 1
				if guess % 5 == 0 or guess > 9:
					target_file.write("DELAY " + str(protection_delay) + "\n")
					target_file.write("ENTER\n")
					target_file.write("DELAY " + str(500) + "\n")
					target_file.write("ALT SPACE\n")
					target_file.write("DELAY " + str(500) + "\n")



except FileNotFoundError:
	print(f"The file '{input_file}' was not found.")
except Exception as e:
	print(f"An error occurred: {str(e)}")
