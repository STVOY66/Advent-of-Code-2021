input_file = open('input.txt', 'r')
input_lines = input_file.readlines()
for index in range(0, len(input_lines)):
    input_lines[index] = input_lines[index].strip().split()

def part_one():
    forwCount = 0
    downCount = 0
    upCount = 0
    for index in range(0, len(input_lines)):
        if input_lines[index][0] == 'forward':
            forwCount += int(input_lines[index][1])
        elif input_lines[index][0] == 'down':
            downCount += int(input_lines[index][1])
        elif input_lines[index][0] == 'up':
            upCount += int(input_lines[index][1])
    finalDepth = downCount - upCount
    print(forwCount*finalDepth)

def part_two():
    forwCount = 0
    aim = 0
    depth = 0
    for index in range(0, len(input_lines)):
        if input_lines[index][0] == 'forward':
            forwCount += int(input_lines[index][1])
            depth += aim*int(input_lines[index][1])
        elif input_lines[index][0] == 'down':
            aim += int(input_lines[index][1])
        elif input_lines[index][0] == 'up':
            aim -= int(input_lines[index][1])
    print(forwCount*depth)

part_two()