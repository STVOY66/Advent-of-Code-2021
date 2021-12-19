import sys, string

input_file = open('input.txt', 'r')
input_lines = input_file.readlines()
for index in range(0, len(input_lines)):
    input_lines[index] = int(input_lines[index].strip())

def part_one() -> int:
    incrCount = 0
    for index in range(1, len(input_lines)):
        if input_lines[index] > input_lines[index-1]:
            incrCount += 1
    return incrCount

def part_two():
    incrCount = 0
    prevSum = input_lines[0] + input_lines[1] + input_lines[2]
    for index in range(2, len(input_lines) - 1):
        newSum = input_lines[index - 1] + input_lines[index] + input_lines[index + 1]
        if prevSum < newSum:
            incrCount += 1
        prevSum = newSum
    return incrCount

if len(sys.argv) == 1:
    print("Please enter \'1\' for part one or \'2\' for part two")
elif len(sys.argv) == 2:
    if int(sys.argv[1]) == 1:
        print("Answer to part one: {}\n".format(part_one()))
    elif int(sys.argv[1]) == 2:
        print("Answer to part two: {}\n".format(part_two()))
    else:
        print("Invalid input, please enter \'1\' for part one or \'2\' for part two")
else:
    print("Too many arguments passed, please enter \'1\' for part one or \'2\' for part two")