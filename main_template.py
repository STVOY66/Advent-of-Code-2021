import sys

input_file = open('input.txt', 'r')
input_lines = input_file.readlines()
for index in range(0, len(input_lines)):
    input_lines[index] = input_lines[index].strip()

def part1():
    pass

def part2():
    pass

if len(sys.argv) == 1:
    print("Please enter \'1\' for part one or \'2\' for part two")
elif len(sys.argv) == 2:
    if int(sys.argv[1]) == 1:
        part1()
    elif int(sys.argv[1]) == 2:
        part2()
    else:
        print("Invalid input, please enter \'1\' for part one or \'2\' for part two")
else:
    print("Too many arguments passed, please enter \'1\' for part one or \'2\' for part two")